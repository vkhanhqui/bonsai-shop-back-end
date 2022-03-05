from app.models.models import AddressTable
from app.utils.db_utils import session


def get_all_addresses_by_user_id(user_id: int):
    addresses = session.query(AddressTable).\
        filter(AddressTable.user_id == user_id).\
        all()
    return addresses
