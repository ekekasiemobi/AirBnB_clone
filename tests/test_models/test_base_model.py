#!/usr/bin/python3

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""
    def test_init(self):
        """Test the __init__ method of the BaseModel class."""
        base = BaseModel()
        
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the base class."""
        base = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(str(base), expected_str)

    def test_save(self):
        """Test the save method of the BaseModel class."""
        base = BaseModel()
        old_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(old_updated_at, base.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        bm = BaseModel(name="Aliyu", number=27)
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict["name"], "Aliyu")
        self.assertEqual(bm_dict["number"], 27)

    def test_instantiation_with_kwargs(self):
        """Test instantiation of BaseModel with keyword arguments."""
        kwargs = {"id": "345", "created_at": "2023-01-01T00:00:00.000000", "updated_at": "2023-01-02T00:00:00.000000"}
        bm = BaseModel(**kwargs)
        self.assertEqual(bm.id, '345')
        self.assertEqual(bm.created_at, datetime(2023, 1, 1))
        self.assertEqual(bm.updated_at, datetime(2023, 1, 2))


if __name__ == '__main__':
    unittest.main()
