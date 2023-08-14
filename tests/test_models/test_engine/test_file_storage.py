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
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.storage.reload()

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_empty_storage(self):
        """ a method that test all storage functionality """
        all_objs = self.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsNotNone(obj)
        self.assertTrue(os.path.isfile('file.json'))

    def test_save(self):
        """Test the save method"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open("file.json", "r") as f:
            data = f.read()
            key = "User.{}".format(user.id)
            self.assertIn(key, data)

    def test_save_method(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            key = "User." + user.id
            self.assertIn(key, data)
            self.assertEqual(data[key], user.to_dict())

    def test_reload_method(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "User." + user.id
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key], user)

    def test_data_integrity(self):
        user = User()
        user.name = "Alice"
        user.email = "alice@example.com"
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        reloaded_user = new_storage.all()["User." + user.id]
        self.assertEqual(user.name, reloaded_user.name)
        self.assertEqual(user.email, reloaded_user.email)

    def test_incorrect_file_path(self):
        original_path = FileStorage.__file_path
        FileStorage.__file_path = "nonexistent.json"
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 0)
        FileStorage.__file_path = original_path

    def test_all_method(self):
        user = User()
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User." + user.id: user})

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

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_from_file(self):
        """ a method that test reload functionality """
        objs = self.storage.all()
        for obj in objs.keys():
            inst = objs[obj]
            self.assertIsNotNone(obj)
            self.assertTrue(inst, dict)
        self.assertTrue(os.path.isfile('file.json'))

    def test_new_method(self):
        user = User()
        self.storage.new(user)
        self.assertIn("User." + user.id, self.storage.all().keys())
        self.assertEqual(user, self.storage.all()["User." + user.id])

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
