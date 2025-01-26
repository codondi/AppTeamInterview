from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from api.dependencies import get_db
from api.auth import verify_admin
from api.schemas import (
    UserCreate, UserResponse,
    RestaurantCreate, RestaurantResponse,
    RatingCreate, RatingResponse
)
from api.services import (
    add_new_user, get_user_by_id, get_all_users, update_user, delete_user,
    add_new_restaurant, get_restaurant_by_id, get_all_restaurants, update_restaurant, delete_restaurant,
    add_new_rating, get_rating_by_id, get_all_ratings, update_rating, delete_rating
)

app = FastAPI()

# User Endpoints
@app.post("/users/", response_model=UserResponse, status_code=201)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return add_new_user(user, db)

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)

@app.get("/users/", response_model=List[UserResponse], dependencies=[Depends(verify_admin)])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@app.put("/users/{user_id}", response_model=UserResponse, dependencies=[Depends(verify_admin)])
def update_user_info(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user(user_id, user, db)

@app.delete("/users/{user_id}", status_code=204, dependencies=[Depends(verify_admin)])
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)

# Restaurant Endpoints
@app.post("/restaurants/", response_model=RestaurantResponse, status_code=201, dependencies=[Depends(verify_admin)])
def add_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return add_new_restaurant(restaurant, db)

@app.get("/restaurants/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return get_restaurant_by_id(restaurant_id, db)

@app.get("/restaurants/", response_model=List[RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return get_all_restaurants(db)

@app.put("/restaurants/{restaurant_id}", response_model=RestaurantResponse, dependencies=[Depends(verify_admin)])
def update_restaurant_info(restaurant_id: int, restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return update_restaurant(restaurant_id, restaurant, db)

@app.delete("/restaurants/{restaurant_id}", status_code=204, dependencies=[Depends(verify_admin)])
def remove_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return delete_restaurant(restaurant_id, db)

# Rating Endpoints
@app.post("/ratings/", response_model=RatingResponse, status_code=201)
def add_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    return add_new_rating(rating, db)

@app.get("/ratings/{rating_id}", response_model=RatingResponse)
def get_rating(rating_id: int, db: Session = Depends(get_db)):
    return get_rating_by_id(rating_id, db)

@app.get("/ratings/", response_model=List[RatingResponse])
def get_ratings(db: Session = Depends(get_db)):
    return get_all_ratings(db)

@app.put("/ratings/{rating_id}", response_model=RatingResponse, dependencies=[Depends(verify_admin)])
def update_rating_info(rating_id: int, rating: RatingCreate, db: Session = Depends(get_db)):
    return update_rating(rating_id, rating, db)

@app.delete("/ratings/{rating_id}", status_code=204, dependencies=[Depends(verify_admin)])
def remove_rating(rating_id: int, db: Session = Depends(get_db)):
    return delete_rating(rating_id, db)