#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import sys
from models.base_model import BaseModel
import json

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """


    __class = ["BaseModel", "FileStorage"]
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
                if not there_is_match:
                    print("** no instance found **")
                    



if __name__ == "__main__":
    if not sys.stdin.isatty():
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()
