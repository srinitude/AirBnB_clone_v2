#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_type == "db":
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
            all_cities = list(models.storage.all(City).values())
            return list(filter((lambda c: c.state_id == self.id), all_cities))
