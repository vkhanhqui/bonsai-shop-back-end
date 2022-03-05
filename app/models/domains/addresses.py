from pydantic import BaseModel, Field


class AddressCity(BaseModel):
    city: str = Field(
        min_length=5, max_length=100,)


class AddressDistrict(BaseModel):
    district: str = Field(
        min_length=5, max_length=100,)


class AddressFullAddress(BaseModel):
    full_address: str = Field(min_length=5,)
