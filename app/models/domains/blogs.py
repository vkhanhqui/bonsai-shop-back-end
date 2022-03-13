from typing import Text
from pydantic import BaseModel, Field


class BlogTitle(BaseModel):
    title: str = Field()


class BlogContent(BaseModel):
    content: Text = Field()


class BlogDescription(BaseModel):
    description: Text = Field()
