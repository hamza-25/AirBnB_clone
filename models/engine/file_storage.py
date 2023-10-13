#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        #class_name = obj.__class__.__name__ + "." + str(obj.id)
        class_name = f"{obj.__class__.__name__}.{str(obj.id)}"
        FileStorage.__objects[class_name] = obj

    def save(self):
        data = {}
        for key, value  in self.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)
    
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for obj in data.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    cls_obj = globals().get(class_name)
                    if cls_obj:
                        ob = cls_obj(**obj)
                        self.new(ob)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return
