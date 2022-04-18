from app.models.models import BillTable
from app.utils.db_utils import session
from sqlalchemy import text
from app.core.config import config


def get_cart(user_id: str):
    bill_status = config.bill_status.get('customer_created')
    bills = session.query(BillTable).\
        filter(
        text("customer_id=:customer_id and bill_status=:bill_status")).\
        params(customer_id=user_id, bill_status=bill_status).all()
    if bills:
        return bills[0]
    return None
