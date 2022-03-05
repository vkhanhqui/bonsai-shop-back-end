from sqlalchemy.orm import contains_eager

from app.models.models import (
    BillTable,
    BillManagementTable,
)
from app.utils.db_utils import session
from app.core.config import config


def get_all_bills():
    bill_status = config.bill_status.get('customer_created')
    bills = session.query(BillTable, BillManagementTable).\
        filter(BillTable.bill_status != bill_status).\
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
