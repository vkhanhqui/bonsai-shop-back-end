from pydantic import BaseModel, Field
from datetime import datetime


class CreateAt(BaseModel):
    created_at: datetime = Field(alias='created_at')


class Message(BaseModel):
    message: str = Field(default='', alias='message')


class UserId(BaseModel):
    user_id: int = Field(alias='user_id')


class RoleId(BaseModel):
    role_id: int = Field(alias='role_id')


class ProductId(BaseModel):
    product_id: int = Field(alias='product_id')


class CategoryId(BaseModel):
    category_id: int = Field(alias='category_id')


class PromotionId(BaseModel):
    promotion_id: int = Field(alias='promotion_id')


class BillId(BaseModel):
    bill_id: int = Field(alias='bill_id')


class BillManagementId(BaseModel):
    billmanagement_id: int = Field(alias='billmanagement_id')


class AddressId(BaseModel):
    address_id: int = Field(alias='address_id')


class BlogId(BaseModel):
    blog_id: int = Field(alias='blog_id')


class RatingId(BaseModel):
    rating_id: int = Field(alias='rating_id')


class CommentId(BaseModel):
    comment_id: int = Field(alias='comment_id')


class ImageId(BaseModel):
    image_id: int = Field(alias='image_id')
