from app.models.models import AddressTable
from app.models.schemas.addresses import AddressInCreate
from app.utils.db_utils import session


def create_address(address_in: AddressInCreate) -> AddressTable:
    new_address = AddressTable(**address_in.dict())
    session.add(new_address)
    try:
        session.flush()
        session.commit()
        return new_address
    except Exception:
        session.rollback()
        raise
