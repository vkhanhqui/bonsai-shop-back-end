from typing import Text
from pydantic import BaseModel, Field


class ProductName(BaseModel):
    product_name: str = Field(
        min_length=2, max_length=100,
        alias='product_name')


class ProductPrice(BaseModel):
    product_price: int = Field(
        alias='product_price')


class Description(BaseModel):
    description: Text = Field(None, alias='description')
