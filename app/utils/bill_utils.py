from app.db.customers.get_user_by_id import get_user_by_id
from app.db.images.get_main_image import get_main_image
from app.utils import (
    file_utils as _file_utils,
)


def get_bills_in_detail(
    bills: list, is_admin: bool = False
):
    response = []
    bill_ids = set()
    for bill in bills:
        bill_dict = bill._asdict()
        bill_table = bill_dict.get('BillTable')
        bill_id = bill_table.bill_id
        if bill_id not in bill_ids:
            bill_ids.add(bill_id)
            bill_managements = bill_table.bill_managements
            bill_resp = {
                'bill_id': bill_id,
                'created_at': bill_table.created_at,
                'bill_status': bill_table.bill_status,
                'customer': get_user_by_id(bill_table.customer_id),
                'bill_managements': []
            }
            if is_admin:
                bill_resp.update({
                    'staff_or_admin': get_user_by_id(
                        bill_table.staff_or_admin_id),
                })
            for bill_management in bill_managements:
                product_id = bill_management.product_id
                main_image = _file_utils.map_image(get_main_image(product_id))
                bill_resp.get('bill_managements').append({
                    'product_id': product_id,
                    'product_name':
                        bill_management.product.product_name,
                    'product_price':
                        bill_management.product.product_price,
                    'number_product': bill_management.number_product,
                    **main_image,
                })
            response.append(bill_resp)
    return response
