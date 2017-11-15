#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
import models


class Review(BaseModel, Base):
    """Representation of Review """
    if models.storage_type == "db":
        __tablename__ = "reviews"

        place_id = Column(String(60),
                          ForeignKey("places.id"))
        user_id = Column(String(60),
                         ForeignKey("users.id"))
        text = Column(String(1024),
                      nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
