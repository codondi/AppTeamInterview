from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from api.dependencies import get_db
from api.schemas import RestaurantCreate, RestaurantResponse, RatingCreate, RatingResponse
from api.services import add_new_restaurant, add_new_rating, fetch_ratings

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Restaurant Rating API"}

@app.post("/restaurants/", response_model=RestaurantResponse, status_code=201)
def add_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return add_new_restaurant(restaurant, db)

@app.post("/ratings/", response_model=RatingResponse, status_code=201)
def add_rating(rating: RatingCreate, db: Session = Depends(get_db)):
    return add_new_rating(rating, db)

@app.get("/ratings/", response_model=List[RatingResponse])
def get_ratings(
    restaurant_id: Optional[int] = None,
    min_rating: Optional[float] = None,
    max_rating: Optional[float] = None,
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return fetch_ratings(restaurant_id, min_rating, max_rating, min_calories, max_calories, db)
