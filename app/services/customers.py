from typing import List
from app.db.admins.update_user_info import update_user_info
# from app.db.bills.create_bill import create_bill
# from app.db.bills.get_bill_by_user_id_and_bill_status import \
#     get_bill_by_user_id_and_bill_status
# from app.db.bills.get_cart import get_cart
# from app.db.bills.remove_items_from_bill import remove_items_from_bill
# from app.db.bills.update_bill_mnm_by_product_id_and_bill_id import \
#     update_bill_mnm_by_product_id_and_bill_id
from app.db.bills.customer_confirm_bill import confirm_bill
from app.db.bills.customer_get_all_bills import get_all_bills
from app.db.bills.get_bill_detail import get_bill_detail
from app.db.customers.get_user_by_id import get_user_by_id
from app.db.admins.create_user import create_user
from app.db.images.get_main_image import get_main_image
from app.models.schemas import (
    admins as _admin_schemas,
    bills as _bills_schemas,
)
from app.models.domains import (
    base as _base_domains,
)
from app.utils import (
    file_utils as _file_utils,
)
# VNPAY
from datetime import datetime
import uuid
from app.services.vnpay import VNPay
from fastapi.responses import RedirectResponse

from app.utils.mail_utils import send_msg_via_sendgrid


VNPAY_RETURN_URL = \
    'http://localhost:8000/bonsai-backend/customers/payment-return'
# get from config
VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'
# get from config
VNPAY_API_URL = 'https://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = '14H33NEJ'  # Website ID in VNPAY System, get from config
# Secret key for create checksum,get from config
VNPAY_HASH_SECRET_KEY = 'NVTDUKXFKKOPKEEQJDUZMTPIXEZZALKS'


class CustomerService():

    def get_user_by_id(self, user_id: str):
        response = get_user_by_id(user_id)
        return response

    def create_customer(
        self, staff_in: _admin_schemas.StaffInCreate
    ) -> _admin_schemas.StaffRespDetail:
        response = create_user(staff_in, role_name='customer')
        return response

    def get_bills(
        self, user_id: str
    ) -> List[_bills_schemas.CustomerAllBillsResp]:
        response = get_all_bills(user_id)
        return response

    def get_bill_detail(
        self, bill_id: str
    ) -> _bills_schemas.CustomerBillDetailResp:
        products = []
        bill_total = 0.0
        bill_detail = get_bill_detail(bill_id)
        for obj in bill_detail:
            product_id = obj.product.product_id
            product_price = obj.product.product_price
            number_product = obj.number_product
            main_image = _file_utils.map_image(get_main_image(product_id))
            bill_total_each_prod = number_product * product_price
            obj_resp = {
                'number_product': number_product,
                'product_price': product_price,
                'product_name': obj.product.product_name,
                'product_id': product_id,
                'bill_total': bill_total_each_prod,
                **main_image
            }
            bill_total += float(bill_total_each_prod)
            products.append(obj_resp)
        response = {
            'bill_id': bill_id,
            'bill_total': bill_total,
            'products': products
        }
        return response

    # def get_cart(
    #     self, user_id: str
    # ) -> _bills_schemas.CustomerBillDetailResp:
    #     cart = get_cart(user_id)
    #     if cart:
    #         return self.get_bill_detail(cart.bill_id)
    #     return None

    # def add_to_cart(
    #     self, card_in: _bills_schemas.CustomerAddCardIn
    # ) -> _base_domains.Message:
    #     user_id = card_in.user_id
    #     product_id = card_in.product_id
    #     number_product = card_in.number_product
    #     bill_status = config.bill_status.get('customer_created')
    #     bill = get_bill_by_user_id_and_bill_status(
    #         user_id, bill_status=bill_status
    #     )
    #     msg_response = 'Created the cart successfully'
    #     if bill:
    #         # add to cart
    #         _ = update_bill_mnm_by_product_id_and_bill_id(
    #             product_id, bill.bill_id,
    #             number_product
    #         )
    #         msg_response = 'Updated the cart successfully'
    #     else:
    #         # create a cart
    #         _ = create_bill(
    #             user_id, product_id,
    #             number_product
    #         )
    #     return {'message': msg_response}

    # def remove_items_from_cart(
    #     self, card_in: _bills_schemas.CustomerRemoveItemsIn
    # ) -> _base_domains.Message:
    #     _ = remove_items_from_bill(**card_in.dict())
    #     return {'message': 'Removed items successfully'}

    # def confirm_bill(
    #     self, bill_in: _bills_schemas.CustomerConfirmBillIn
    # ) -> _base_domains.Message:
    #     bill_status = config.bill_status.get('customer_confirmed')
    #     _ = update_bill_by_id(
    #         bill_in.bill_id, bill_status,
    #         bill_in.address_id
    #     )
    #     return {'message': bill_status}

    # new flow
    def confirm_bill(
        self, current_user,
        card_in: _bills_schemas.CustomerConfirmBillIn
    ) -> _base_domains.Message:
        # create a cart
        new_bill = confirm_bill(
            **{'user_id': current_user.user_id},
            **card_in.dict(exclude={'total_price'})
        )
        total_price = '{:20,.2f}'\
            .format(card_in.total_price)\
            .replace('.00', '').strip()
        _ = send_msg_via_sendgrid(
            template_id='d-71a538eac9374d26a564e2060116408c',
            email_to=current_user.email,
            dynamic_template_data={
                "total_price": total_price
            }
        )
        return {'message': new_bill.bill_id}

    def update_user_info(
        self, current_user,
        info_in: _admin_schemas.StaffInUpdate
    ) -> _base_domains.Message:
        _ = update_user_info(
            current_user.user_id, info_in
        )
        return {'message': 'Update user info successfully'}

    def payment(
        self,
        vn_amount, order_info
    ):
        # Process input data and build url payment
        order_type = 'other'
        order_id = str(uuid.uuid1())
        amount = vn_amount
        bank_code = 'NCB'
        language = 'vn'
        # Build URL Payment
        vnp = VNPay()
        vnp.requestData['vnp_Version'] = '2.1.0'
        vnp.requestData['vnp_Command'] = 'pay'
        vnp.requestData['vnp_TmnCode'] = VNPAY_TMN_CODE
        vnp.requestData['vnp_Amount'] = amount * 100
        vnp.requestData['vnp_CurrCode'] = 'VND'
        vnp.requestData['vnp_TxnRef'] = order_id
        vnp.requestData['vnp_OrderInfo'] = order_info
        vnp.requestData['vnp_OrderType'] = order_type
        # Check language, default: vn
        if language and language != '':
            vnp.requestData['vnp_Locale'] = language
        else:
            vnp.requestData['vnp_Locale'] = 'vn'
            # Check bank_code, if bank_code is empty,
            # customer will be selected bank on VNPAY
        if bank_code and bank_code != "":
            vnp.requestData['vnp_BankCode'] = bank_code

        vnp.requestData['vnp_CreateDate'] = datetime.now().strftime(
            '%Y%m%d%H%M%S')  # 20150410063022
        vnp.requestData['vnp_IpAddr'] = '127.0.0.1'
        vnp.requestData['vnp_ReturnUrl'] = VNPAY_RETURN_URL
        vnpay_payment_url = vnp.get_payment_url(
            VNPAY_PAYMENT_URL, VNPAY_HASH_SECRET_KEY)
        return vnpay_payment_url

    def payment_return(
        self,
        vnp_Amount, vnp_BankCode,
        vnp_BankTranNo, vnp_CardType,
        vnp_OrderInfo, vnp_PayDate,
        vnp_ResponseCode, vnp_TmnCode,
        vnp_TransactionNo, vnp_TransactionStatus,
        vnp_TxnRef, vnp_SecureHash
    ):
        inputData = {
            "vnp_TxnRef": vnp_TxnRef,
            "vnp_Amount": vnp_Amount,
            "vnp_BankCode": vnp_BankCode,
            "vnp_BankTranNo": vnp_BankTranNo,
            "vnp_CardType": vnp_CardType,
            "vnp_OrderInfo": vnp_OrderInfo,
            "vnp_PayDate": vnp_PayDate,
            "vnp_ResponseCode": vnp_ResponseCode,
            "vnp_TmnCode": vnp_TmnCode,
            "vnp_TransactionNo": vnp_TransactionNo,
            "vnp_TransactionStatus": vnp_TransactionStatus,
            "vnp_TxnRef": vnp_TxnRef,
            "vnp_SecureHash": vnp_SecureHash
        }
        if inputData:
            vnp = VNPay()
            vnp.responseData = inputData
            order_id = inputData['vnp_TxnRef']
            amount = int(inputData['vnp_Amount']) / 100
            order_desc = inputData['vnp_OrderInfo']
            vnp_TransactionNo = inputData['vnp_TransactionNo']
            vnp_ResponseCode = inputData['vnp_ResponseCode']
            vnp_TmnCode = inputData['vnp_TmnCode']
            vnp_PayDate = inputData['vnp_PayDate']
            vnp_BankCode = inputData['vnp_BankCode']
            vnp_CardType = inputData['vnp_CardType']
            if vnp.validate_response(VNPAY_HASH_SECRET_KEY):
                if vnp_ResponseCode == "00":
                    # return (
                    #     "payment_return.html",
                    #     {
                    #         "title": "Kết quả thanh toán",
                    #         "result": "Thành công",
                    #         "order_id": order_id,
                    #         "amount": amount,
                    #         "order_desc": order_desc,
                    #         "vnp_TransactionNo": vnp_TransactionNo,
                    #         "vnp_ResponseCode": vnp_ResponseCode
                    #     }
                    # )
                    return RedirectResponse(
                        "http://localhost:3000?isVNPaySuccess=true")
                else:
                    return (
                        "payment_return.html",
                        {
                            "title": "Kết quả thanh toán",
                            "result": "Lỗi",
                            "order_id": order_id,
                            "amount": amount,
                            "order_desc": order_desc,
                            "vnp_TransactionNo": vnp_TransactionNo,
                            "vnp_ResponseCode": vnp_ResponseCode
                        }
                    )
            else:
                return (
                    "payment_return.html",
                    {
                        "title": "Kết quả thanh toán",
                        "result": "Lỗi",
                        "order_id": order_id,
                        "amount": amount,
                        "order_desc": order_desc,
                        "vnp_TransactionNo": vnp_TransactionNo,
                        "vnp_ResponseCode": vnp_ResponseCode,
                        "msg": "Sai checksum"
                    }
                )
        else:
            return (
                "payment_return.html",
                {"title": "Kết quả thanh toán", "result": ""}
            )
