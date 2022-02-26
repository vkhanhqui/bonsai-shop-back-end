from app.models.domains import (
    users as _users_domain,
    base as _base,
)


class StaffInCreate(
    _users_domain.UserUsername, _users_domain.UserPwd,
    _users_domain.FirstName, _users_domain.LastName,
    _users_domain.Email, _users_domain.Birthday,
):
    pass


class StaffRespDetail(
    _users_domain.UserUsername, _users_domain.FirstName,
    _users_domain.LastName, _users_domain.Email,
    _users_domain.Birthday, _base.RoleId,
    _base.UserId,
):

    class Config:
        orm_mode = True
