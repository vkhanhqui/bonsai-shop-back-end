from fastapi import HTTPException
from app.db.ratings.create_rating import create_rating
from app.db.ratings.delete_rating import delete_rating
from app.db.ratings.get_all_ratings import get_all_ratings
from app.db.ratings.get_rating_by_prod_and_user import \
    get_rating_by_prod_and_user
from app.db.ratings.update_rating import \
    update_rating_as_customer, update_rating_as_staff
from app.models.schemas import (
    ratings as _rating_schemas
)
from app.utils import (
    auth_utils as _auth_utils
)


class RatingService():

    def create_rating(
        self, current_user,
        rating_in: _rating_schemas.RatingInCreate
    ):
        user_id = current_user.user_id
        rating = get_rating_by_prod_and_user(rating_in.product_id, user_id)
        if rating:
            raise HTTPException(
                status_code=400, detail='Already rated this product'
            )
        _ = create_rating(user_id, rating_in)
        return {'message': 'Created successfully'}

    def get_all_ratings(self, product_id: int):
        response = get_all_ratings(product_id)
        return response

    def update_rating_as_customer(
        self, current_user,
        rating_in: _rating_schemas.RatingCustomerInUpdate
    ):
        response = update_rating_as_customer(current_user.user_id, rating_in)
        return response

    def update_rating_as_staff(
        self, current_user,
        rating_in: _rating_schemas.RatingStaffInUpdate
    ):
        response = update_rating_as_staff(current_user.user_id, rating_in)
        return response

    def delete_rating(
        self, current_user,
        rating_id: int
    ):
        _auth_utils.is_admin_or_staff(
            current_user.user_id, is_raise_err=True
        )
        _ = delete_rating(rating_id)
        return {'message': 'Delete successfully'}
