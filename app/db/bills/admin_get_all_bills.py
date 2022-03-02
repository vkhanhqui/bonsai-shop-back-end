from app.models.models import (
    BillTable,
    BillManagementTable,
)
from app.utils.db_utils import session
from sqlalchemy.orm import contains_eager


def get_all_bills():
    bills = session.query(BillTable, BillManagementTable).\
        join(BillTable.bill_managements).\
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
