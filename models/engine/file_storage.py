#!/usr/bin/python3
"""Define module provides a FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class FileStorage:
    """Representation of FileStorage class that managing
    file-based storage of objects.

    Attributes:
        __file_path (str): The path to the file where objects are stored.
        __objects (dict): contain all obj

    Methods:
        all(): Return a dictionary containing all stored objects.
        save(): Serialize and save the stored objects to the file.
        reload(): Deserialize and load objects from the file.
        new(obj): Create a new object and add it to the storage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Create a new object and add it to the storage.

        Args:
            obj: The object to be added to the storage.
        """
        class_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[class_name] = obj

    def save(self):
        """Serialize and save the stored objects to the file.
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize and load objects from the file.
        """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for obj in data.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    cls_obj = globals().get(class_name)
                    if cls_obj:
                        ob = cls_obj(**obj)
                        self.new(ob)
        except FileNotFoundError:
            return
