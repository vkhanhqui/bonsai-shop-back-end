from typing import List
from app.models.domains import (
    products as _products_domain,
    base as _base_domain,
    bills as _bills_domain,
    images as _images_domain,
)
from app.models.schemas import (
    admins as _admins_schemas,
)


class BillManagementRespDetail(
    _base_domain.ProductId, _products_domain.ProductName,
    _products_domain.ProductPrice, _bills_domain.BillManagementNumberProduct,
    _images_domain.ImagePath,
):

    class Config:
        orm_mode = True


class AdminBillRespDetail(
    _base_domain.CreateAt, _base_domain.BillId,
    _bills_domain.BillStatus
):
    bill_managements: List[BillManagementRespDetail]
    staff_or_admin: _admins_schemas.StaffRespDetail = None
    customer: _admins_schemas.StaffRespDetail

    class Config:
        orm_mode = True


class CustomerAllBillsResp(
    _base_domain.CreateAt, _base_domain.BillId,
    _bills_domain.BillStatus
):

    class Config:
        orm_mode = True


class CustomerBillDetail(
    _images_domain.ImagePath, _bills_domain.BillManagementNumberProduct,
    _products_domain.ProductPrice, _products_domain.ProductName,
    _base_domain.ProductId, _bills_domain.BillTotal,
):
    pass


class CustomerBillDetailResp(
    _bills_domain.BillTotal, _base_domain.BillId,
):
    products: List[CustomerBillDetail]

    class Config:
        orm_mode = True


class CustomerAddCardIn(
    _base_domain.UserId, _base_domain.ProductId,
    _bills_domain.BillManagementNumberProduct
):
    pass


class CustomerRemoveItemsIn(
    _base_domain.BillId, _base_domain.ProductId,
    _bills_domain.BillManagementNumberProduct
):
    pass


class CustomerConfirmBillIn(
    _base_domain.BillId, _base_domain.AddressId,
):
    pass
