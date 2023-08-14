#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
"""
import os
import json
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dictionary(self):
        """Test if the all() method returns a dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        """Test the new() method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = json.load(f)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, data)

    def test_reload(self):
        """Test the reload() method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Clear current storage instance and reload from the file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_all_empty_storage(self):
        """Test all() method with empty storage"""
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsNotNone(obj)
        self.assertTrue(os.path.isfile('file.json'))

    def test_reload_with_arg(self):
        """Test reload() method with an argument"""
        with self.assertRaises(TypeError):
            self.storage.reload(None)

    def test_reload_from_file(self):
        """Test reloading from a file"""
        objs = self.storage.all()
        for obj in objs.values():
            self.assertIsNotNone(obj)
            self.assertIsInstance(obj, dict)
        self.assertTrue(os.path.isfile('file.json'))

    def test_instance_deletion(self):
        """Test deletion of an object instance"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        del obj
        self.storage.reload()
        self.assertNotIn(obj_key, self.storage.all())

    def test_new_multiple_objects(self):
        """Test creating and saving multiple object types"""
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()
        obj1_key = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        obj2_key = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        obj3_key = "{}.{}".format(obj3.__class__.__name__, obj3.id)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(obj1_key, self.storage.all())
        self.assertIn(obj2_key, self.storage.all())
        self.assertIn(obj3_key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
