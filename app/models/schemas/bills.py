from typing import List
from app.models.domains import (
    products as _products_domain,
    base as _base,
    bills as _bills_domain,
)
from app.models.schemas import (
    admins as _admins_schemas,
)


class BillManagementRespDetail(
    _base.ProductId, _products_domain.ProductName,
    _products_domain.ProductPrice, _bills_domain.BillManagementNumberProduct,
):

    class Config:
        orm_mode = True


class AdminBillRespDetail(
    _base.CreateAt, _base.BillId,
    _bills_domain.BillStatus
):
    bill_managements: List[BillManagementRespDetail]
    staff_or_admin: _admins_schemas.StaffRespDetail = None
    customer: _admins_schemas.StaffRespDetail

    class Config:
        orm_mode = True
