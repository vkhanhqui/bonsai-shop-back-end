from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# db connection
YOUR_DATABASE_USERNAME = 'root'
YOUR_DATABASE_PASSWORD = 'root'
YOUR_DATABASE_NAME = 'bonsai_db'
engine=create_engine(
    f"mysql+pymysql://{YOUR_DATABASE_USERNAME}:{YOUR_DATABASE_PASSWORD}@localhost:3306/{YOUR_DATABASE_NAME}",
    echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


# models
from sqlalchemy import String, Boolean, Integer, Column, Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)

Base.metadata.create_all(engine)
# API
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List


app=FastAPI()


class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True


db=SessionLocal()


@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(Item).all()

    return items


@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(Item).filter(Item.id==item_id).first()
    return item


@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(Item).filter(Item.name==item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")
    new_item=Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )
    db.add(new_item)
    db.commit()
    return new_item


@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(Item).filter(Item.id==item_id).first()
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.description=item.description
    item_to_update.on_offer=item.on_offer
    db.commit()
    return item_to_update


@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(Item).filter(Item.id==item_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    db.delete(item_to_delete)
    db.commit()
    return item_to_delete