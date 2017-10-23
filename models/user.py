#!/usr/bin/python
""" holds class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'

    email =  Column(String(128), nullable=False)
    password =  Column(String(128), nullable=False)
    first_name =  Column(String(128), nullable=False)
    last_name =  Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
