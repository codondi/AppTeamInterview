from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=1)

class UserResponse(UserCreate):
    id: int
    class Config:
        orm_mode = True

class RestaurantCreate(BaseModel):
    name: str = Field(..., min_length=1)
    cuisine_type: str = Field(..., min_length=1)

class RestaurantResponse(RestaurantCreate):
    id: int
    class Config:
        orm_mode = True

class RatingCreate(BaseModel):
    user_id: int
    restaurant_id: int
    rating: float = Field(..., ge=0, le=5)
    calories: int = Field(..., gt=0)
    message: Optional[str] = None
    meal_time: Optional[datetime] = None

class RatingResponse(RatingCreate):
    id: int
    class Config:
        orm_mode = True
