from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.addresses import AddressService
from app.models.domains import (
    base as _base_domains
)
from app.models.schemas import (
    addresses as _address_schemas,
)


router = APIRouter()
address_service = AddressService()


@router.post(
    "/create-address",
    status_code=status.HTTP_201_CREATED,
    response_model=_address_schemas.AddressRespDetail
)
async def create_address(
    address_in: _address_schemas.AddressInCreate
):
    return address_service.create_address(address_in)


@router.get(
    '/get-all-addresses/{user_id}',
    response_model=List[_address_schemas.AddressRespDetail],
    status_code=status.HTTP_200_OK
)
async def get_all_addresses(user_id: int):
    return address_service.get_all_addresses_by_user_id(user_id)


@router.put(
    "/update-address",
    status_code=status.HTTP_200_OK,
    response_model=_address_schemas.AddressInUpdate
)
async def update_address(
    address_in: _address_schemas.AddressInUpdate
):
    return address_service.update_address(address_in)


@router.delete(
    "/delete-address/{address_id}",
    status_code=status.HTTP_200_OK,
    response_model=_base_domains.Message
)
async def delete_address(
    address_id: int
):
    return address_service.delete_address(address_id)
