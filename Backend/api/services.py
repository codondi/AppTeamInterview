from sqlalchemy.orm import Session
from entities.models import User, Restaurant, RestaurantRating
from api.schemas import UserCreate, RestaurantCreate, RatingCreate
from datetime import datetime

# User Services
def add_new_user(user: UserCreate, db: Session):
    new_user = User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def update_user(user_id: int, user: UserCreate, db: Session):
    db_user = get_user_by_id(user_id, db)
    if db_user:
        db_user.username = user.username
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(user_id: int, db: Session):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()

# Restaurant Services
def add_new_restaurant(restaurant: RestaurantCreate, db: Session):
    new_restaurant = Restaurant(name=restaurant.name, cuisine_type=restaurant.cuisine_type)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant

def get_restaurant_by_id(restaurant_id: int, db: Session):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

def get_all_restaurants(db: Session):
    return db.query(Restaurant).all()

def update_restaurant(restaurant_id: int, restaurant: RestaurantCreate, db: Session):
    db_restaurant = get_restaurant_by_id(restaurant_id, db)
    if db_restaurant:
        db_restaurant.name = restaurant.name
        db_restaurant.cuisine_type = restaurant.cuisine_type
        db.commit()
        db.refresh(db_restaurant)
    return db_restaurant

def delete_restaurant(restaurant_id: int, db: Session):
    db.query(Restaurant).filter(Restaurant.id == restaurant_id).delete()
    db.commit()

# Rating Services
def add_new_rating(rating: RatingCreate, db: Session):
    new_rating = RestaurantRating(
        user_id=rating.user_id,
        restaurant_id=rating.restaurant_id,
        rating=rating.rating,
        calories=rating.calories,
        message=rating.message,
        meal_time=rating.meal_time or datetime.utcnow()
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating

def get_rating_by_id(rating_id: int, db: Session):
    return db.query(RestaurantRating).filter(RestaurantRating.id == rating_id).first()

def get_all_ratings(db: Session):
    return db.query(RestaurantRating).all()

def update_rating(rating_id: int, rating: RatingCreate, db: Session):
    db_rating = get_rating_by_id(rating_id, db)
    if db_rating:
        db_rating.rating = rating.rating
        db_rating.calories = rating.calories
        db_rating.message = rating.message
        db_rating.meal_time = rating.meal_time or datetime.utcnow()
        db.commit()
        db.refresh(db_rating)
    return db_rating

def delete_rating(rating_id: int, db: Session):
    db.query(RestaurantRating).filter(RestaurantRating.id == rating_id).delete()
    db.commit()