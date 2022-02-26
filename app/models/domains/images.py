from pydantic import BaseModel, Field


class ImagePath(BaseModel):
    image_path: str = Field(
        alias='image_path')
