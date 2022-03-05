
from app.models.models import BillTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_bill_by_user_id_and_bill_status(
    user_id: int, bill_status: str
) -> BillTable:
    query_text = 'customer_id=:user_id and bill_status=:bill_status'
    bills = session.query(BillTable).\
        filter(text(query_text)).\
        params(user_id=user_id, bill_status=bill_status).\
        all()
    if bills:
        return bills[0]
    return None
