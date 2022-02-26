from fastapi import (
    Depends,
    HTTPException,
    status
)
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from app.utils import auth_utils as _auth_utils
from app.core.config import config
from app.models.schemas import auth as _auth_schemas


class LoginService():

    def login(
        self, form_data: OAuth2PasswordRequestForm = Depends()
    ) -> _auth_schemas.Token:
        user = _auth_utils.authenticate_user(
            form_data.username, form_data.password
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(
            minutes=config.access_token_expire_minutes
        )
        access_token = _auth_utils.create_access_token(
            data={
                "username": user.username,
                "user_id": user.user_id,
                "email": user.email,
                "last_name": user.last_name,
                "first_name": user.first_name,
            },
            expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
