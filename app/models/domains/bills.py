from pydantic import BaseModel, Field


class BillManagementNumberProduct(BaseModel):
    number_product: int = Field(default=0)


class BillStatus(BaseModel):
    bill_status: str = Field()
