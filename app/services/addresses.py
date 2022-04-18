from app.db.addresses.create_address import create_address
from app.db.addresses.delete_address import delete_address
from app.db.addresses.get_all_addresses_by_user_id import \
    get_all_addresses_by_user_id
from app.db.addresses.update_address import update_address
from app.models.schemas import addresses as _address_schemas


class AddressService():

    def create_address(
        self, current_user,
        address_in: _address_schemas.AddressInCreate
    ):
        response = create_address(
            current_user.user_id, address_in
        )
        return response

    def get_all_addresses_by_user_id(self, user_id: int):
        response = get_all_addresses_by_user_id(user_id)
        return response

    def update_address(self, address_in: _address_schemas.AddressInUpdate):
        response = update_address(address_in)
        return response

    def delete_address(self, address_id: int):
        _ = delete_address(address_id)
        return {'message': 'Delete successfully'}
