from sqlalchemy.orm import Session
from entities.models import Restaurant, RestaurantRating
from api.schemas import RestaurantCreate, RatingCreate

def add_new_restaurant(restaurant: RestaurantCreate, db: Session):
    existing_restaurant = db.query(Restaurant).filter(Restaurant.name == restaurant.name).first()
    if existing_restaurant:
        return existing_restaurant  # Prevent duplicate entries
    new_restaurant = Restaurant(name=restaurant.name, cuisine_type=restaurant.cuisine_type)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant

def add_new_rating(rating: RatingCreate, db: Session):
    restaurant = db.query(Restaurant).filter(Restaurant.id == rating.restaurant_id).first()
    if not restaurant:
        raise ValueError("Restaurant not found")
    new_rating = RestaurantRating(
        restaurant_id=rating.restaurant_id,
        rating=rating.rating,
        calories=rating.calories,
        meal_time=rating.meal_time or datetime.utcnow()
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating

def fetch_ratings(restaurant_id, min_rating, max_rating, min_calories, max_calories, db: Session):
    query = db.query(RestaurantRating)
    if restaurant_id is not None:
        query = query.filter(RestaurantRating.restaurant_id == restaurant_id)
    if min_rating is not None:
        query = query.filter(RestaurantRating.rating >= min_rating)
    if max_rating is not None:
        query = query.filter(RestaurantRating.rating <= max_rating)
    if min_calories is not None:
        query = query.filter(RestaurantRating.calories >= min_calories)
    if max_calories is not None:
        query = query.filter(RestaurantRating.calories <= max_calories)
    return query.all()
