from pydantic import BaseModel, Field


class BillManagementNumberProduct(BaseModel):
    number_product: int = Field(default=0)


class BillStatus(BaseModel):
    bill_status: str = Field()


class BillTotal(BaseModel):
    bill_total: float = Field(default=0.0)
