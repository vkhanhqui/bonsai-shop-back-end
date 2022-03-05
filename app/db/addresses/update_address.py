from app.models.models import AddressTable
from app.models.schemas.addresses import AddressInUpdate
from app.utils.db_utils import session


def update_address(address_in: AddressInUpdate):
    try:
        _ = session.query(AddressTable)\
            .filter(AddressTable.address_id == address_in.address_id)\
            .update({
                AddressTable.full_address: address_in.full_address,
                AddressTable.city: address_in.city,
                AddressTable.district: address_in.district,
                AddressTable.phone_number: address_in.phone_number,
            })
        session.commit()
        return address_in
    except Exception:
        session.rollback()
        raise
