from typing import List
from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app.services.customers import CustomerService
from app.models.schemas import (
    admins as _admin_schemas,
    bills as _bills_schemas,
    auth as _auth_schemas
)
from app.models.domains import (
    base as _base_domains,
)
from app.utils import auth_utils as _auth_utils


router = APIRouter()
customer_service = CustomerService()


# @router.get(
#     '/get-user-by-id/{user_id}',
#     response_model=_admin_schemas.StaffRespDetail,
#     status_code=status.HTTP_200_OK
# )
# async def get_user_by_id(user_id: str):
#     return customer_service.get_user_by_id(user_id)


@router.post(
    "/create-customer",
    status_code=status.HTTP_201_CREATED,
    response_model=_admin_schemas.StaffRespDetail
)
async def create_customer(
    customer_in: _admin_schemas.StaffInCreate
):
    return customer_service.create_customer(customer_in)


@router.get(
    '/get-bills',
    response_model=List[_bills_schemas.CustomerAllBillsResp],
    status_code=status.HTTP_200_OK
)
async def get_bills(
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return customer_service.get_bills(current_user.user_id)


@router.get(
    '/get-bill-detail/{bill_id}',
    response_model=_bills_schemas.CustomerBillDetailResp,
    status_code=status.HTTP_200_OK
)
async def get_bill_detail(
    bill_id: str,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return customer_service.get_bill_detail(bill_id)


# @router.get(
#     '/get-cart/{user_id}',
#     response_model=_bills_schemas.CustomerBillDetailResp,
#     status_code=status.HTTP_200_OK
# )
# async def get_cart(user_id: str):
#     return customer_service.get_cart(user_id)


# @router.post(
#     '/add-to-cart',
#     response_model=_base_domains.Message,
#     status_code=status.HTTP_200_OK
# )
# async def add_to_cart(card_in: _bills_schemas.CustomerAddCardIn):
#     return customer_service.add_to_cart(card_in)


# @router.put(
#     '/remove-items-from-cart',
#     response_model=_base_domains.Message,
#     status_code=status.HTTP_200_OK
# )
# async def remove_items_from_cart(
#     card_in: _bills_schemas.CustomerRemoveItemsIn
# ):
#     return customer_service.remove_items_from_cart(card_in)


# @router.put(
#     '/confirm-bill',
#     response_model=_base_domains.Message,
#     status_code=status.HTTP_200_OK
# )
# async def confirm_bill(
#     bill_in: _bills_schemas.CustomerConfirmBillIn,
# ):
#     return customer_service.confirm_bill(bill_in)

# new flow
@router.post(
    '/confirm-bill',
    response_model=_base_domains.Message,
    status_code=status.HTTP_200_OK
)
async def confirm_bill(
    bill_in: _bills_schemas.CustomerConfirmBillIn,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return customer_service.confirm_bill(current_user, bill_in)


@router.put(
    '/update-user-info',
    response_model=_base_domains.Message,
    status_code=status.HTTP_200_OK
)
async def update_user_info(
    info_in: _admin_schemas.StaffInUpdate,
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return customer_service.update_user_info(
        current_user, info_in
    )


@router.get(
    "/get-user-info",
    response_model=_admin_schemas.StaffRespDetail
)
async def read_users_me(
    current_user: _auth_schemas.User =
        Depends(_auth_utils.get_current_user)
):
    return current_user
