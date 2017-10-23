#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Review(BaseModel):
    """Representation of Review """
    __tablename__ = "reviews"

    place_id = Column(String(60),
                      ForeignKey"place_id",
                      nullable=False)
    user_id = Column(String(60),
                      ForeignKey"user_id",
                      nullable=False)
    text = Column(String(1024),nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
