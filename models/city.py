#!/usr/bin/python3
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import sqlalchemy


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_type == "db":
        __tablename__ = "cities"

        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey("states.id"))
        places = relationship("Place",
                              backref="cities",
                              cascade="delete")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
