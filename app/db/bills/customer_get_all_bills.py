from app.models.models import BillTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_all_bills(user_id: str):
    bills = session.query(BillTable).filter(text("customer_id=:user_id")).\
        params(user_id=user_id).all()
    return bills
