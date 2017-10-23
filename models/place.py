#!/usr/bin/python
""" holds class Place"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

class Place(BaseModel):
    """Representation of Place """
    city_id = Column(String(60),
                     ForeignKey"cities.id",
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey"user.id",
                     nullable=False)
    name =  Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
