from fastapi import (
    Depends,
    APIRouter,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from app.services.login import LoginService

# from app.utils import auth_utils as _auth_utils
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


# demo
# @router.get("/users/me/", response_model=_auth_schemas.User)
# async def read_users_me(
#     current_user: _auth_schemas.User =
#         Depends(_auth_utils.get_current_user)
# ):
#     return current_user
