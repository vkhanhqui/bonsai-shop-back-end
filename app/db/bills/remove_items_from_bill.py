from app.db.bills.delete_bill_mnm_by_product_id_and_bill_id import \
    delete_bill_mnm_by_product_id_and_bill_id
from app.db.bills.get_bill_mnm_by_product_id_and_bill_id import \
    get_bill_mnm_by_product_id_and_bill_id
from app.utils.db_utils import session


def remove_items_from_bill(
    product_id: int, bill_id: int,
    number_product: int
):
    try:
        bill_mnm = get_bill_mnm_by_product_id_and_bill_id(
            product_id, bill_id
        )
        if bill_mnm:
            bill_mnm.number_product -= number_product
            if bill_mnm.number_product < 1:
                bill_mnm.number_product = 0
                _ = delete_bill_mnm_by_product_id_and_bill_id(
                    product_id, bill_id
                )
            session.commit()
    except Exception:
        session.rollback()
        raise
