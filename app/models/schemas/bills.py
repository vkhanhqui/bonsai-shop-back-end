from typing import List
from app.models.domains import (
    products as _products_domain,
    base as _base_domain,
    bills as _bills_domain,
    images as _images_domain,
    addresses as _addresses_domain,
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
    _bills_domain.BillStatus, _addresses_domain.AddressFullAddress,
    _addresses_domain.AddressCity, _addresses_domain.AddressDistrict,
    _addresses_domain.AddressPhoneNumber,
):
    bill_managements: List[BillManagementRespDetail]
    staff_or_admin: _admins_schemas.StaffRespDetail = None
    customer: _admins_schemas.StaffRespDetail
    total_price: int = 0
    stt: int = 1

    class Config:
        orm_mode = True


class CustomerAllBillsResp(
    _base_domain.BillId,
    _bills_domain.BillStatus
):
    stt: int = 0
    created_at: str = ''

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


# class CustomerConfirmBillIn(
#     _base_domain.BillId, _base_domain.AddressId,
# ):
#     pass


# new flow
class ItemIn(
    _base_domain.ProductId, _bills_domain.BillManagementNumberProduct
):
    pass


class CustomerConfirmBillIn(
    _base_domain.AddressId,
):
    items: List[ItemIn]
    total_price: float
