from app.models.models import BillTable
from app.utils.db_utils import session


def update_bill_by_id(
    bill_id: int, bill_status: str,
    address_id: int = None
):
    try:
        update_query = {BillTable.bill_status: bill_status}
        if address_id:
            update_query.update({'address_id': address_id})
        _ = session.query(BillTable)\
            .filter(BillTable.bill_id == bill_id)\
            .update(update_query)
        session.commit()
    except Exception:
        session.rollback()
        raise
