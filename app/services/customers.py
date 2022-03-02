from typing import List
from app.db.bills.customer_get_all_bills import get_all_bills
from app.db.bills.get_bill_detail import get_bill_detail
from app.db.bills.get_cart import get_cart
from app.db.customers.get_user_by_id import get_user_by_id
from app.db.admins.create_user import create_user
from app.db.images.get_main_image import get_main_image
from app.models.schemas import (
    admins as _admin_schemas,
    bills as _bills_schemas,
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
            main_image = get_main_image(product_id)
            bill_total_each_prod = number_product * product_price
            obj_resp = {
                'number_product': number_product,
                'product_price': product_price,
                'product_name': obj.product.product_name,
                'image_path': main_image,
                'product_id': product_id,
                'bill_total': bill_total_each_prod,
            }
            bill_total += float(bill_total_each_prod)
            products.append(obj_resp)
        response = {
            'bill_id': bill_id,
            'bill_total': bill_total,
            'products': products
        }
        return response

    def get_cart(
        self, user_id: str
    ) -> _bills_schemas.CustomerBillDetailResp:
        cart = get_cart(user_id)
        if cart:
            return self.get_bill_detail(cart.bill_id)
        return None
