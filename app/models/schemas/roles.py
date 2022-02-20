from app.models.domains import (
    roles as _roles_domain,
    base as _base,
)


class RoleInCreate(
    _roles_domain.RoleName,
):
    pass


class RoleRespDetail(
    _roles_domain.RoleName, _base.RoleId,
    _base.CreateAt,
):

    class Config:
        orm_mode = True


class RoleInUpdate(
    _roles_domain.RoleName, _base.RoleId,
):
    pass
