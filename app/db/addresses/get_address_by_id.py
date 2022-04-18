from app.models.models import AddressTable
from app.utils.db_utils import session


def get_address_by_id(address_id: int) -> AddressTable:
    addresses = session.query(AddressTable).\
        filter(AddressTable.address_id == address_id).\
        all()
    if addresses:
        return addresses[0]
    return None
