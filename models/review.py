#!/usr/bin/python3
"""defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """representation of Review Class
        Attributes:
            place_id : can be empty
            user_id : can be empty
            text : can be empty
    """
    place_id = ""
    user_id = ""
    text = ""
