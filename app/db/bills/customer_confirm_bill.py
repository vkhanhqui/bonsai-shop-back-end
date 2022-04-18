from app.db.addresses.get_address_by_id import get_address_by_id
from app.models.models import (
    BillManagementTable,
    BillTable,
)
from app.utils.db_utils import session
from app.core.config import config


def confirm_bill(
    user_id: int, address_id: int,
    items: dict
):
    bill_status = config.bill_status.get('customer_confirmed')
    address = get_address_by_id(address_id)
    address_in = {
        'city': address.city,
        'district': address.district,
        'phone_number': address.phone_number,
        'full_address': address.full_address
    }
    new_bill = BillTable(
        customer_id=user_id, bill_status=bill_status,
        **address_in
    )
    session.add(new_bill)
    try:
        session.flush()
        session.commit()
        for item in items:
            _ = create_bill_mnm(
                new_bill.bill_id, item.get('product_id'),
                item.get('number_product')
            )
        return new_bill
    except Exception:
        session.rollback()
        raise


def create_bill_mnm(
    bill_id: int, product_id: int,
    number_product: int
):
    new_bill_mnm = BillManagementTable(
        bill_id=bill_id, product_id=product_id,
        number_product=number_product
    )
    session.add(new_bill_mnm)
    try:
        session.flush()
        session.commit()
        return new_bill_mnm
    except Exception:
        session.rollback()
        raise
