from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base
from Customer import Customer
from Restaurant import Restaurant

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_rel = relationship('Customer', back_populates='reviews_rel')
    restaurant_rel = relationship('Restaurant', back_populates='reviews_rel')

    def __init__(self, content, customer, restaurant):
        self.rating = content
        self.customer_rel = customer
        self.restaurant_rel = restaurant



