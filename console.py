#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import sys

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
    
    def do_quit(self, arg):
        """Quits the HBnB console."""
        return True
    
    def do_EOF(self, arg):
        """Exits the HBnB console."""
        return True

    def do_create(self, args):
        words = args.split()
        if len(words) == 0:
            print("** class name missing **")
        elif words[0] not in self.__class:
            print("** class doesn't exist **")
        else:
            pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
