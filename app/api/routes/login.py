from fastapi import (
    Depends,
    APIRouter,
    status
)
from fastapi.security import OAuth2PasswordRequestForm

from app.services.login import LoginService
from app.models.schemas import auth as _auth_schemas


router = APIRouter()
login_service = LoginService()


@router.post(
    "/token",
    status_code=status.HTTP_200_OK,
    response_model=_auth_schemas.Token
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return login_service.login(form_data)
