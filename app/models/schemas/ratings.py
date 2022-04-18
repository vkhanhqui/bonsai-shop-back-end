from app.models.domains import (
    ratings as _ratings_domain,
    base as _base,
)


class RatingInCreate(
    _base.Message, _base.ProductId,
    _ratings_domain.StartNumber
):
    pass


class RatingRespDetail(
    _base.Message, _base.ProductId,
    _base.UserId, _ratings_domain.StartNumber,
    _base.CreateAt, _base.RatingId,
):

    class Config:
        orm_mode = True


class RatingCustomerInUpdate(
    _base.Message, _base.ProductId,
    _ratings_domain.StartNumber
):
    pass


class RatingStaffInUpdate(
    _base.Message, _base.RatingId,
    _ratings_domain.StartNumber,
):
    pass
