from sqlalchemy import (
    String,
    Integer,
    Column,
    Date,
    DateTime,
    DECIMAL,
    Text,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.connection import db_connection


class UserTable(db_connection.Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    hashed_password = Column(String(200), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    birthday = Column(Date, nullable=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    addresses = relationship("AddressTable")
    blogs = relationship("BlogTable")
    comments = relationship("CommentTable")
    rating = relationship("RatingTable")


class RoleTable(db_connection.Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.today)
    users = relationship("UserTable")


class ProductTable(db_connection.Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False)
    product_price = Column(DECIMAL, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.today)
    bill_managements = relationship("BillManagementTable")
    images = relationship("ImageTable")
    rating = relationship("RatingTable")
    category_id = Column(Integer, ForeignKey('categories.category_id'))


class ImageTable(db_connection.Base):
    __tablename__ = 'images'
    image_id = Column(Integer, primary_key=True)
    image_path = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    product_id = Column(Integer, ForeignKey('products.product_id'))


class CategoryTable(db_connection.Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.today)
    products = relationship("ProductTable")
    promotion_id = Column(
        Integer, ForeignKey('promotions.promotion_id'),
        nullable=True,
    )


class PromotionTable(db_connection.Base):
    __tablename__ = 'promotions'
    promotion_id = Column(Integer, primary_key=True)
    promo_name = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.today)
    discount_percent = Column(Float, nullable=False)
    categories = relationship("CategoryTable")


class BillTable(db_connection.Base):
    __tablename__ = 'bills'
    bill_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.today)
    bill_status = Column(String(100), nullable=False)
    city = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)
    phone_number = Column(String(13), nullable=True)
    full_address = Column(Text, nullable=True)
    customer_id = Column(Integer, ForeignKey('users.user_id'))
    staff_or_admin_id = Column(
        Integer, ForeignKey('users.user_id'),
        nullable=True
    )
    bill_managements = relationship("BillManagementTable")


class BillManagementTable(db_connection.Base):
    __tablename__ = 'billmanagements'
    product_id = Column(ForeignKey('products.product_id'), primary_key=True)
    bill_id = Column(ForeignKey('bills.bill_id'), primary_key=True)
    number_product = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    bills = relationship("BillTable")
    product = relationship("ProductTable")


class AddressTable(db_connection.Base):
    __tablename__ = 'addresses'
    address_id = Column(Integer, primary_key=True)
    city = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    phone_number = Column(String(13), nullable=False)
    full_address = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    user_id = Column(Integer, ForeignKey('users.user_id'))


class BlogTable(db_connection.Base):
    __tablename__ = 'blogs'
    blog_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content_in_markdown = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    staff_or_admin_id = Column(Integer, ForeignKey('users.user_id'))


class RatingTable(db_connection.Base):
    __tablename__ = 'rating'
    rating_id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=True)
    star_number = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    comments = relationship("CommentTable")


class CommentTable(db_connection.Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.today)
    staff_or_customer_id = Column(Integer, ForeignKey('users.user_id'))
    rating_id = Column(Integer, ForeignKey('rating.rating_id'))
