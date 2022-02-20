from pydantic import BaseModel, Field


class RoleName(BaseModel):
    role_name: str = Field(
        min_length=2, max_length=20,
        alias='role_name')
