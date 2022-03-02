from app.models.models import BillTable
from app.utils.db_utils import session


def update_bill_by_id(bill_id: int, bill_status: str):
    _ = session.query(BillTable)\
      .filter(BillTable.bill_id == bill_id)\
      .update({BillTable.bill_status: bill_status})
    session.commit()
