#!/usr/bin/python3
import uuid
import datetime
"""representation of BaseModel"""


class BaseModel():
    """Base Model Class"""

    def __init__(self, my_number="", name=""):
        """init BaseModel initializing
        """
        self.my_number = my_number
        self.name = name
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updted_at = datetime.datetime.now()

    def save(self):
        """save function that update updted_at attrb
        """
        self.updted_at = datetime.datetime.now()

    def to_dict(self):
        """get dict of attrb object

        Returns:
            return a dict
        """
        return {
            "my_number": self.my_number,
            "name": self.name,
            "__class__": self.__class__.__name__,
            "updted_at": self.updted_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat()
        }

    def __str__(self):
        """__str__ funtion that represent the object

        Returns:
            string contain info about object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
