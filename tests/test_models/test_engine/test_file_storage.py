#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
"""
import unittest
import os
import json
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dictionary(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = json.load(f)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, data)

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Clear current storage instance and reload from the file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
