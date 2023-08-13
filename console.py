#!/usr/bin/env python3
"""Define the HBnB console."""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import json
import models
from models import storage
from models.base_model import BaseModel
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Define the HBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
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
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def precmd(self, line):
        """Preprocess the command line before execution."""
        parts = line.split('.', 1)
        if len(parts) == 2:
            command = parts[0]
            args = parts[1].split('(', 1)
            cmd = args[0]
            new_line = cmd + " " + command
            if len(args) == 2:
                args = args[1].split(')', 1)
                args = args[0].split(",")
                a_id = args[0].strip()
                new_line = cmd + " " + command + " " + a_id
                if len(args) > 1:
                    others = args[1:]
                    s = ""
                    for c in others:
                        s += c
                    s = s.replace("\"", "").strip()
                    new_line = cmd + " " + command + " " + a_id + " " + s
            return new_line
        return line

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.__models:
            print("** class doesn't exist **")
            return

        count = 0
        objects_dict = models.storage.all()
        for key, value in objects_dict.items():
            if value.__class__.__name__ == class_name:
                count += 1

        print(count)

    def do_create(self, arg):
        """Instantiate a new object of BaseModel and
        store it in the JSON file.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Display the string representation of a class
        instance based on class name and id.
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects_dict = models.storage.all()
            instance_key = "{}.{}".format(args[0], args[1])
            instance = objects_dict.get(instance_key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

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
        elif args[0] not in HBNBCommand.__models:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects_dict = models.storage.all()
            instance_key = "{}.{}".format(args[0], args[1])
            instance = objects_dict.get(instance_key)
            if instance:
                del objects_dict[instance_key]
                models.storage.save()
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

        if obj_key not in obj_dict:
            print("** no instance found **")
            return

        instance = obj_dict[obj_key]

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
