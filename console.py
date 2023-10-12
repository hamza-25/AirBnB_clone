#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

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
    


if __name__ == "__main__":
    HBNBCommand().cmdloop()