#!/usr/bin/env python3

import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def emptyline(self):
        pass

    def create_instance(self, argument):
        """Instantiate a new object of BaseModel and store it in the JSON file"""
        arguments = argument.split()
        if not arguments:
            print("** Missing class name **")
            return

        class_name = arguments[0]
        if class_name not in self.classes:
            print("** Class does not exist **")
            return

        new_object = self.classes[class_name]()
        new_object.save()
        print(new_object.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

