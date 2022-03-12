from typing import List
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
from app.core.config import config
from app.utils import (
    file_utils as _file_utils,
)


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
        self, card_in: _bills_schemas.CustomerConfirmBillIn
    ) -> _base_domains.Message:
        bill_status = config.bill_status.get('customer_confirmed')
        # create a cart
        _ = confirm_bill(**card_in.dict())
        return {'message': bill_status}
