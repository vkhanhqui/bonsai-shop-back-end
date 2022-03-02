from typing import List
from fastapi import (
    APIRouter,
    status,
)

from app.services.customers import CustomerService
from app.models.schemas import (
    admins as _admin_schemas,
    bills as _bills_schemas,
)


router = APIRouter()
customer_service = CustomerService()


@router.get(
    '/get-user-by-id/{user_id}',
    response_model=_admin_schemas.StaffRespDetail,
    status_code=status.HTTP_200_OK
)
async def get_user_by_id(user_id: str):
    return customer_service.get_user_by_id(user_id)


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
    '/get-bills/{user_id}',
    response_model=List[_bills_schemas.CustomerAllBillsResp],
    status_code=status.HTTP_200_OK
)
async def get_bills(user_id: str):
    return customer_service.get_bills(user_id)


@router.get(
    '/get-bill-detail/{bill_id}',
    response_model=_bills_schemas.CustomerBillDetailResp,
    status_code=status.HTTP_200_OK
)
async def get_bill_detail(bill_id: str):
    return customer_service.get_bill_detail(bill_id)
