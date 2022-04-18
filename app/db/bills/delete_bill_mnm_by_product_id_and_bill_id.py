from app.models.models import BillManagementTable
from app.utils.db_utils import session


def delete_bill_mnm_by_product_id_and_bill_id(
    product_id: int, bill_id: int
) -> None:
    try:
        _ = session.query(BillManagementTable)\
         .filter(
            BillManagementTable.product_id == product_id
            and BillManagementTable.bill_id == bill_id
            )\
         .delete()
        _ = session.commit()
    except Exception:
        session.rollback()
        raise
