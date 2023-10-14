#!/usr/bin/python3
"""Defines the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of State Class
        Attributes:
            name : can be empty
    """
    name = ""
