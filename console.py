#!/usr/bin/env python3

import cmd
import json
import sys
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __models = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

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

    def create_instance(self, arg):
        """Instantiate a new object of BaseModel and store it in the JSON file"""
        args = arg.split()
        if not arguments:
            print("** Missing class name **")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("** Class does not exist **")
            return

        new_object = self.classes[class_name]()
        new_object.save()
        print(new_object.id)

    def do_show(self, arg):
        """
        Display the string representation of a class instance based on class name and id.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) <= 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        obj_key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if obj_key in obj_dict:
            instance_repr = str(obj_dict[obj_key])
            print(instance_repr)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Display string representations of all instances based on the class name.
        """
        objects_dict = models.storage.all()
        instance_list = []

        if not arg:
            for key in objects_dict:
               instance_list.append(str(objects_dict[key]))
        else:
            class_name = arg.strip()
            if class_name in self.__models:
                for key, value in objects_dict.items():
                    if value.__class__.__name__ == class_name:
                        instance_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return

        print(instance_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
