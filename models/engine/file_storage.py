#!/usr/bin/python3
import json
import os
class fileStorage:
    __file_path = "c:/Users/hamza/Desktop/airbnb/models/engine/file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def save(self):
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def new(self, obj):
        class_name = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[class_name] = obj.__dict__

    def reload(self):
        if os.path.exists(self.__file_path) and os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
                print(self.__objects)
                print(type(self.__objects))
