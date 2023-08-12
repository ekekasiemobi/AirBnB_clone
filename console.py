#!/usr/bin/env python3
"""Define the HBnB console."""
import cmd
import json
from models.user import User
import sys
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Define the HBnB command interpreter.
    Attributes:
        promp (str): The command prompt.
    """
    prompt = "(hbnb) "
    __models = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
        }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Instantiate a new object of BaseModel and
        store it in the JSON file
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Display the string representation of a class
        instance based on class name and id.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_all(self, arg):
        """
        Display string representations of all instances
        based on the class name.
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

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"

            if class_name not in self.__models:
                print("** class doesn't exist **")
            else:
                obj_dict = storage.all()
                if key in obj_dict:
                    del obj_dict[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
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
            instance = obj_dict[obj_key]
        else:
            print("** no instance found **")
            return

        if len(args) <= 2:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) <= 3:
            print("** value missing **")
            return

        attribute_value = args[3]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
