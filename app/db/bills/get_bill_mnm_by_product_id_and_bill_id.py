
from app.models.models import BillManagementTable
from app.utils.db_utils import session
from sqlalchemy import text


def get_bill_mnm_by_product_id_and_bill_id(
    product_id: int, bill_id: int
) -> BillManagementTable:
    query_text = 'product_id=:product_id and bill_id=:bill_id'
    bill_mnm = session.query(BillManagementTable).\
        filter(text(query_text)).\
        params(product_id=product_id, bill_id=bill_id).\
        all()
    if bill_mnm:
        return bill_mnm[0]
    return None
