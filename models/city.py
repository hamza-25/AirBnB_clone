#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of Class City

        Attributes:
            state_id : can be empty
            name : can be empty
    """
    state_id = ""
    name = ""
