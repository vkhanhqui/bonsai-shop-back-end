from app.models.models import BillManagementTable
from app.utils.db_utils import session
from sqlalchemy.orm import contains_eager
from sqlalchemy import text


def get_bill_detail(bill_id: str):
    bills = session.query(BillManagementTable).\
        join(BillManagementTable.product).\
        options(
            contains_eager(BillManagementTable.product)).\
        filter(text("bill_id=:bill_id")).params(bill_id=bill_id).all()
    return bills
