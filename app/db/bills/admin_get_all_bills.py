from sqlalchemy.orm import contains_eager

from app.models.models import (
    BillTable,
    BillManagementTable,
)
from app.utils.db_utils import session


def get_all_bills(customer_id: int = 0):
    bills = session.query(BillTable, BillManagementTable)
    if customer_id > 0:
        bills = bills.filter(
            BillTable.customer_id == customer_id
        )
    bills = bills.join(BillTable.bill_managements).\
        options(
            contains_eager(BillTable.bill_managements)).\
        join(BillManagementTable.product).\
        options(
            contains_eager(
                BillManagementTable.product
            )
        ).\
        all()
    return bills
