#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """Representation of state """
    __tablename__ = "states"

    name = Column(String(128),
                  nullable=False)
    storage_type = os.getenv("HBNB_TYPE_STORAGE")
    if storage_type == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="delete")
    else:
        @property
        def cities(self):
            

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
