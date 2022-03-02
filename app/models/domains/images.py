from pydantic import BaseModel, Field


class ImagePath(BaseModel):
    image_path: str = Field(
        None, alias='image_path')
