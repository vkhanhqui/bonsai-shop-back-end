from pydantic import BaseModel, Field
from datetime import date


class UserUsername(BaseModel):
    username: str = Field(
        min_length=2, max_length=20,
        alias='username')


class UserPwd(BaseModel):
    password: str = Field(
        min_length=8, max_length=20,
        alias='password')


class Birthday(BaseModel):
    birthday: date = Field(None, alias='birthday')


class FirstName(BaseModel):
    first_name: str = Field(
        min_length=2,
        alias='first_name')


class LastName(BaseModel):
    last_name: str = Field(
        min_length=2,
        alias='last_name')
