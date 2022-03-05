from app.models.domains import (
    addresses as _addresses_domain,
    base as _base,
)


class AddressInCreate(
    _addresses_domain.AddressFullAddress, _addresses_domain.AddressCity,
    _addresses_domain.AddressDistrict, _base.UserId,
    _addresses_domain.AddressPhoneNumber,
):
    pass


class AddressRespDetail(
    _addresses_domain.AddressFullAddress, _addresses_domain.AddressCity,
    _addresses_domain.AddressDistrict, _base.UserId,
    _base.AddressId, _addresses_domain.AddressPhoneNumber,
):

    class Config:
        orm_mode = True


class AddressInUpdate(
    _addresses_domain.AddressFullAddress, _addresses_domain.AddressCity,
    _addresses_domain.AddressDistrict, _base.AddressId,
    _addresses_domain.AddressPhoneNumber,
):
    pass
