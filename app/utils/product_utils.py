from app.db.ratings.get_all_ratings import get_all_ratings


def get_total_stars(product_id: int):
    ratings = get_all_ratings(product_id)
    stars = list(
        map(lambda x: x.star_number, ratings)
    )
    total = len(stars)
    if total < 1:
        total = 1
    star_number = sum(stars)/total
    return star_number
