#!/usr/bin/python3
import uuid
from datetime import datetime
"""representation of BaseModel"""


class BaseModel():
    """Base Model Class"""

    my_number = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init BaseModel initializing
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        dt_fmt = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(value, dt_fmt)
                    elif key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value, dt_fmt)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updted_at = datetime.now()

    def save(self):
        """save function that update updted_at attrb
        """
        self.updted_at = datetime.now()

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
