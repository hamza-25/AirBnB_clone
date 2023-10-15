#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    __class = [
            "BaseModel", "Amenity", "User",
            "City", "Place", "Review", "State"
            ]
    prompt = "(hbnb) "

    def default(self, args):
        """default method that execute if none of the method in the input
        """
        class_name = ["all()", "count()", "show()", "destroy()"]
        str_split = args.split('.')
        if len(str_split) == 2:
            if str_split[0] in self.__class and str_split[1] in class_name:
                expr = "self.do_{}".format(str_split[1][:-2])
                eval(expr)(str_split[0])
            elif '"' in str_split[1] and ',' not in str_split[1]:
                object_name, method_and_args = str_split
                method_and_args = method_and_args.strip('()')
                method, arguments = method_and_args.split('(')
                arguments = arguments.rstrip(')')
                if (object_name in self.__class
                        and "{}()".format(method) in class_name):
                    objects = storage.all()
                    key_format = "{}.{}".format(object_name, arguments[1:-1])
                    if key_format in objects:
                        expr = "self.do_{}".format(method)
                        param = "{} {}".format(object_name, arguments[1:-1])
                        eval(expr)(param)
                    else:
                        print("** no instance found **")
            elif ',' in str_split[1] and '{' not in str_split[1]:
                method_param = str_split[1].split('(')
                id_att_value = method_param[1].split(',')
                uid, att, value = id_att_value
                uid, att = uid[1:-1], att[2:-1]
                if '"' in value:
                    value = int(value[2:-2])
                else:
                    value = int(value[1:-1])
                objects = storage.all()
                key_format = "{}.{}".format(str_split[0], uid)
                if key_format in objects:
                    expr = "self.do_{}".format(method_param[0])
                    param = "{} {} {} {}".format(str_split[0], uid, att, value)
                    eval(expr)(param)
        else:
            print("***Unknown syntax: {}".format(arg))

    def do_count(self, args):
        """count methods
            attr:
                count: that count the number of obj
            Return:
                print count
        """
        count = 0
        str_split = args.split()
        if args:
            class_name = str_split[0]
            objects = storage.all()
            for obj in objects.values():
                if class_name == obj.__class__.__name__:
                    count += 1
        print(count)

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
        """Create a new object and add it to the storage.

        Args:
            args (list): A list of arguments containing object information.

        """
        words = args.split()
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in self.__class:
            print("** class doesn't exist **")
        else:
            obj = eval(args)()
            obj.save()
            print(obj.id)
            # storage.save()

    def do_show(self, args):
        """Show details of a specific object.

        Args:
            args (list): A list of arguments specifying the object to display.

        """
        words = args.split()
        if not args:
            print("** class name missing **")
        elif words[0] not in self.__class:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2:
            with open("file.json") as file:
                data = json.load(file)
            # data = storage.all()
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
        """Delete an object from the storage.

        Args:
            args (list): A list of arguments specifying the object to delete.

        """
        words = args.split()
        if not args:
            print("** class name missing **")
        elif words[0] not in self.__class:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2:
            with open("file.json") as file:
                data = json.load(file)
            # data = storage.all()
                there_is_match = False
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0] and words[1] == k_s[1]:
                        del data[key]
                        with open("file.json", "w") as file:
                            json.dump(data, file)
                        # storage.save()
                        return
                if not there_is_match:
                    print("** no instance found **")

    def do_all(self, args):
        """List all objects currently stored in 'file.json'.

        Args:
            args (list): Additional optional arguments.

        """
        words = args.split()
        if not args:
            with open("file.json") as file:
                data = json.load(file)
            # data = storage.all()
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
            # data = storage.all()
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
        """Update an existing object's attributes in the storage.

        Args:
            args (list): A list of arguments containing object information.

        """
        words = args.split()
        if not args:
            print("** class name missing **")
        elif words[0] not in self.__class:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2:
            with open("file.json") as file:
                data = json.load(file)
            # data = storage.all()
                there_is_match = False
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0] and words[1] == k_s[1]:
                        there_is_match = True
                if not there_is_match:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
        elif len(words) == 3:
            print("** value missing **")
        elif len(words) >= 4:
            with open("file.json") as file:
                data = json.load(file)
            # data = storage.all()
                for key in data.keys():
                    k_s = key.split('.')
                    if words[0] == k_s[0] and words[1] == k_s[1]:
                        data[key][words[2]] = words[3].strip('"')
            with open("file.json", "w") as f:
                json.dump(data, f)
            # storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
