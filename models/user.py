#!/usr/bin/python3
"""Define user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class
        Attributes:
            email : can be empty
            password : can be empty
            first_name : can be empty
            last_name : can be empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
