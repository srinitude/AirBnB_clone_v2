#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os

class State(BaseModel, Base):
    """Representation of state """

    storage_type = os.getenv("HBNB_TYPE_STORAGE")
    if storage_type == "db":
        __tablename__ = "states"

        name = Column(String(128),
                  nullable=False)
        cities = relationship("City",
                              backref="state",
                              cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            objects = models.storage.all()
            for object in objects:
                

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
