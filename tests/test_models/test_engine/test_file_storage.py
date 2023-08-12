#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.storage.reload()

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

    def test_all_empty_storage(self):
        """ a method that test all storage functionality """
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsNotNone(obj)
        self.assertTrue(os.path.isfile('file.json'))

    def test_new(self):
        """Test the new method"""
        user = User()
        self.storage.new(user)
        key = "User.{}".format(user.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open("file.json", "r") as f:
            data = f.read()
            key = "User.{}".format(user.id)
            self.assertIn(key, data)

    def test_reload(self):
        """Test the reload method"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        key = "User.{}".format(user.id)
        self.assertIn(key, self.storage.all())

    def check_json_file(self, content):
        """ check if the content of a file is json """
        try:
            json.loads(content)
            return True
        except json.JSONDecodeError:
            return False

    def test_all_empty_storage(self):
        """ a method that test all storage functionality """
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsNotNone(obj)
        self.assertTrue(os.path.isfile('file.json'))

if __name__ == '__main__':
    unittest.main()
