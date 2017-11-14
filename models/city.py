#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = "cities"

    name = Column(String(128),
                  nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id"))

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
