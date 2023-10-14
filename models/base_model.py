#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime
"""Define base_model"""


class BaseModel():
    """Representation BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """init BaseModel initializing
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        dt_fmt = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(value, dt_fmt)
                    else:
                        self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """save function that update updated_at attrb
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """get dict of attrb object

        Returns:
            return a dict
        """
        objt_dict = self.__dict__.copy()
        objt_dict["__class__"] = self.__class__.__name__
        objt_dict["created_at"] = self.created_at.isoformat()
        objt_dict["updated_at"] = self.updated_at.isoformat()
        return objt_dict

    def __str__(self):
        """__str__ funtion that represent the object

        Returns:
            string contain info about object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
