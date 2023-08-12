#!/usr/bin/python3

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

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

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

if __name__ == '__main__':
    unittest.main()
