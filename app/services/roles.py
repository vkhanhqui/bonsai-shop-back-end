from app.db.roles.create_role import create_role
from app.db.roles.delete_role import delete_role
from app.db.roles.get_all_roles import get_all_roles
from app.db.roles.update_role import update_role
from app.models.schemas import roles as _role_schemas
from app.utils import auth_utils as _auth_utils


class RoleService():

    def create_role(self, role_in: _role_schemas.RoleInCreate):
        response = create_role(role_in)
        return response

    def get_all_roles(self, current_user):
        _auth_utils.is_admin(
            current_user.user_id, is_raise_err=True
        )
        response = get_all_roles()
        return response

    def update_role(self, role_in: _role_schemas.RoleInUpdate):
        response = update_role(role_in)
        return response

    def delete_role(self, role_id: int):
        _ = delete_role(role_id)
        return {'message': 'Delete successfully'}
