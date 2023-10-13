#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
#from models.engine.file_storage import FileStorage
import json

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """


    __class = ["BaseModel", "FileStorage", "User"]
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    def do_quit(self, args):
        """Quits the HBnB console."""
        return True
    
    def do_EOF(self, args):
        """Exits the HBnB console."""
        return True

    def do_create(self, args):
        words = args.split()
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in self.__class:
            print("** class doesn't exist **")
        else:
            obj = eval(args)()
            obj.save()
            print(obj.id)
    
    def do_show(self, args):
        """show method"""
        words = args.split()
        if not args:
            print("** class name missing **")
        elif  words[0] not in self.__class:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2:
            with open("file.json") as file:
                data = json.load(file)
                there_is_match = False
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0] and words[1] == k_s[1]:
                        there_is_match = True
                        class_name = data[key]["__class__"]
                        del data[key]["__class__"]
                        cls_obj = globals().get(class_name)
                        if cls_obj:
                            ob = cls_obj(**data[key])
                            print(ob)
                if not there_is_match:
                    print("** no instance found **")

    def do_destroy(self, args):
        """destroy method"""
        words = args.split()
        if not args:
            print("** class name missing **")
        elif  words[0] not in self.__class:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2:
            with open("file.json") as file:
                data = json.load(file)
                there_is_match = False
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0] and words[1] == k_s[1]:
                        del data[key]
                        with open("file.json", "w") as file:
                            json.dump(data, file)
                        return
                if not there_is_match:
                    print("** no instance found **")

    def do_all(self, args):
        """all method"""
        words = args.split()
        if not args:
             with open("file.json") as file:
                data = json.load(file)
                for key in data.keys():
                    class_name = data[key]["__class__"]
                    del data[key]["__class__"]
                    cls_obj = globals().get(class_name)
                    if cls_obj:
                        ob = cls_obj(**data[key])
                        print(ob)
        elif words[0] not in self.__class and len(words) > 0:
            print("** class doesn't exist **")
        elif words[0] in self.__class and len(words) > 0:
            with open("file.json") as file:
                data = json.load(file)
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0]:
                        class_name = data[key]["__class__"]
                        del data[key]["__class__"]
                        cls_obj = globals().get(class_name)
                        if cls_obj:
                            ob = cls_obj(**data[key])
                            print(ob)

    def do_update(self, args):
        words = args.split()
        if not args:
            print("** class name missing **")
        elif  words[0] not in self.__class:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2:
            with open("file.json") as file:
                data = json.load(file)
                there_is_match = False
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0] and words[1] == k_s[1]:
                        there_is_match = True
                        #class_name = data[key]["__class__"]
                        #del data[key]["__class__"]
                        #cls_obj = globals().get(class_name)
                        #if cls_obj:
                        #    ob = cls_obj(**data[key])
                        #    print(ob)
                if not there_is_match:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
        elif len(words) == 3:
            print("** value missing **")
        elif len(words) >= 4:
           pass 



if __name__ == "__main__":
    if not sys.stdin.isatty():
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()
