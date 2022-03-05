from app.db.bills.create_bill import create_bill_mnm
from app.db.bills.get_bill_mnm_by_product_id_and_bill_id import \
    get_bill_mnm_by_product_id_and_bill_id
from app.utils.db_utils import session


def update_bill_mnm_by_product_id_and_bill_id(
    product_id: int, bill_id: int,
    number_product: int
):
    try:
        bill_mnm = get_bill_mnm_by_product_id_and_bill_id(
            product_id, bill_id
        )
        if bill_mnm:
            bill_mnm.number_product += number_product
        else:
            _ = create_bill_mnm(
                bill_id, product_id,
                number_product
            )
        session.commit()
    except Exception:
        session.rollback()
        raise
