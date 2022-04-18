from pydantic import BaseModel, Field


class CategoryName(BaseModel):
    category_name: str = Field(
        min_length=2, max_length=50,)
