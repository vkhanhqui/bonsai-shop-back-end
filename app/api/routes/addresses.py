from typing import List
from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app.services.addresses import AddressService
from app.models.domains import (
    base as _base_domains
)
from app.models.schemas import (
    addresses as _address_schemas,
    auth as _auth_schemas
)
from app.utils import auth_utils as _auth_utils


router = APIRouter()
address_service = AddressService()


@router.post(
    "/create-address",
    status_code=status.HTTP_201_CREATED,
    response_model=_address_schemas.AddressRespDetail
)
async def create_address(
    address_in: _address_schemas.AddressInCreate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return address_service.create_address(current_user, address_in)


@router.get(
    '/get-all-addresses',
    response_model=List[_address_schemas.AddressRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_addresses(
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return address_service.get_all_addresses_by_user_id(
        current_user.user_id
    )


@router.put(
    "/update-address",
    status_code=status.HTTP_200_OK,
    response_model=_address_schemas.AddressInUpdate
)
async def update_address(
    address_in: _address_schemas.AddressInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return address_service.update_address(address_in)


@router.delete(
    "/delete-address/{address_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_address(
    address_id: int,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return address_service.delete_address(address_id)
