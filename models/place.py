#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class
        Attributes:
            city_id : can be empty
            user_id : can be empty
            name : can be empty
            description : can be empty
            number_rooms : default value 0
            number_bathrooms : default value 0
            max_guest : default value 0
            price_by_night : default value 0
            latitude : default value 0.0
            longitude : default value 0.0
            amenity_ids : can be empty
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
