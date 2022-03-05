from app.models.models import (
    BillManagementTable,
    BillTable,
)
from app.utils.db_utils import session
from app.core.config import config


def create_bill(
    customer_id: int, product_id: int,
    number_product: int
):
    bill_status = config.bill_status.get('customer_created')
    new_bill = BillTable(
        customer_id=customer_id, bill_status=bill_status
    )
    session.add(new_bill)
    try:
        session.flush()
        session.commit()
        _ = create_bill_mnm(
            new_bill.bill_id, product_id,
            number_product
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
