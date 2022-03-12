from app.db.addresses.get_address_by_id import get_address_by_id
from app.models.models import BillTable
from app.utils.db_utils import session


def update_bill_by_id(
    bill_id: int, bill_status: str,
    address_id: int = None, staff_or_admin_id: int = None
):
    try:
        update_query = {BillTable.bill_status: bill_status}
        if staff_or_admin_id:
            update_query.update({
                'staff_or_admin_id': staff_or_admin_id
            })
        if address_id:
            address = get_address_by_id(address_id)
            if address:
                update_query.update({
                    'city': address.city,
                    'district': address.district,
                    'phone_number': address.phone_number,
                    'full_address': address.full_address
                })
        _ = session.query(BillTable)\
            .filter(BillTable.bill_id == bill_id)\
            .update(update_query)
        session.commit()
    except Exception:
        session.rollback()
        raise
