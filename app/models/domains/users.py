from pydantic import BaseModel, Field


class UserUsername(BaseModel):
    username: str = Field(
        min_length=2, max_length=20,
        alias='username')


class UserPwd(BaseModel):
    password: str = Field(
        min_length=8, max_length=20,
        alias='password')
