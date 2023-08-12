#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Represent a storage engine.
    Attributes:
        __file_path (str): The name ofthe file tosave objects to.
        __objects (dict): A dictionary of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set __objects obj with key <obj._class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialized __objects to the JSON file __file_path."""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it existes."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    if cls_name == "User":
                        obj = User(**value)
                    elif cls_name == "Place":
                        obj = Place(**value)
                    elif cls_name == "State":
                        obj = State(**value)
                    elif cls_name == "City":
                        obj = City(**value)
                    elif cls_name == "Amenity":
                        obj = Amenity(**value)
                    elif cls_name == "Review":
                        obj = Review(**value)
                    else:
                        continue
                    self.new(obj)
        except FileNotFoundError:
            pass
