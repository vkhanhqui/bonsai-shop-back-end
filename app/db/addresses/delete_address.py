from app.models.models import AddressTable
from app.utils.db_utils import session


def delete_address(address_id: int) -> None:
    try:
        _ = session.query(AddressTable)\
         .filter(AddressTable.address_id == address_id)\
         .delete()
        _ = session.commit()
    except Exception:
        session.rollback()
        raise
