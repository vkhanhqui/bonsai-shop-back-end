from fastapi import (
    APIRouter,
    status,
)

from app.services.customers import CustomerService
from app.models.schemas import (
    admin as _admin_schemas,
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
