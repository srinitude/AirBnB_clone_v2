#!/usr/bin/python3
""" holds class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
import models

class Place(BaseModel, Base):
    """Representation of Place """
    if models.storage_type == "db":
        __tablename__ = "places"

        city_id = Column(String(60),
                         ForeignKey("cities.id"))
        user_id = Column(String(60),
                         ForeignKey("user.id"))
        name =  Column(String(128),
                       nullable=False)
        description = Column(String(1024),
                             nullable=True)
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
        latitude = Column(Float,
                          nullable=True)
        longitude = Column(Float,
                           nullable=True)
    else:
        city_id = ""
        user_id = ""
        name = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
