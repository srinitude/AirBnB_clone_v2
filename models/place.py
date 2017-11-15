#!/usr/bin/python3
""" holds class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import Float
from sqlalchemy.orm import relationship
import models

if models.storage_type == "db":
    class PlaceAmenity(Base):
        __tablename__ = "place_amenity"
        place_id = Column(String(80),
                          ForeignKey("places.id"),
                          primary_key=True,
                          nullable=False)
        amenity_id = Column(String(80),
                            ForeignKey("amenities.id"),
                            primary_key=True,
                            nullable=False)
        metadata = Base.metadata


class Place(BaseModel, Base):
    """Representation of Place """
    if models.storage_type == "db":
        __tablename__ = "places"

        city_id = Column(String(60),
                         ForeignKey("cities.id"))
        user_id = Column(String(60),
                         ForeignKey("users.id"))
        name = Column(String(128),
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
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review",
                               backref="place",
                               cascade="delete")
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0

        @property
        def reviews(self):
            """Returns respective list of reviews"""
            all_reviews = models.storage.all(Review)
            return list(filter((lambda c: c.place_id == self.id), all_reviews))

        @property
        def amenities(self):
            """Returns respective list of reviews"""
            amenities = models.storage.all(Amenity)
            return list(filter((lambda c: c.place_id == self.id), amenities))

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
