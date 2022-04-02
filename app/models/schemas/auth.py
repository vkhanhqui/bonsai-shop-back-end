from app.models.domains import (
    users as _users_domain,
    base as _base,
)


class Token(
    _base.UserId, _users_domain.UserUsername,
    _users_domain.FirstName, _users_domain.LastName,
    _users_domain.Email, _base.RoleId
):
    access_token: str
    token_type: str


class User(
    _base.UserId, _users_domain.UserUsername,
    _users_domain.FirstName, _users_domain.LastName,
    _users_domain.Email
):

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
