#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[class_name] = obj
    
    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)
    
    def reload(self):
        #if os.path.exists(FileStorage.__file_path) and os.path.isfile(FileStorage.__file_path):
            #with open(FileStorage.__file_path, "r") as file:
                #FileStorage.__objects = json.load(file)
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r") as file:
                    data = json.load(file)
                    FileStorage.__objects = data
            except (FileNotFoundError, json.JSONDecodeError) as e:
                return
