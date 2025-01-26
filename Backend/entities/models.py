from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    role = Column(String, default="user", nullable=False)
    ratings = relationship("RestaurantRating", back_populates="user")

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    cuisine_type = Column(String, nullable=False)
    ratings = relationship("RestaurantRating", back_populates="restaurant")

class RestaurantRating(Base):
    __tablename__ = "restaurant_ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    rating = Column(Float, nullable=False)
    calories = Column(Integer, nullable=False)
    message = Column(String, nullable=True)
    meal_time = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="ratings")
    restaurant = relationship("Restaurant", back_populates="ratings")
