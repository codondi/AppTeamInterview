from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    cuisine_type = Column(String, index=True, nullable=False)
    ratings = relationship("RestaurantRating", back_populates="restaurant", cascade="all, delete-orphan")

class RestaurantRating(Base):
    __tablename__ = "restaurant_ratings"
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    rating = Column(Float, nullable=False)
    calories = Column(Integer, nullable=False)
    meal_time = Column(DateTime, default=datetime.utcnow, nullable=False)
    restaurant = relationship("Restaurant", back_populates="ratings")
