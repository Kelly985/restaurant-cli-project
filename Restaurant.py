from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reviews_rel = relationship('Review', back_populates='restaurant_rel')

    def __init__(self, name):
        self.name = name
