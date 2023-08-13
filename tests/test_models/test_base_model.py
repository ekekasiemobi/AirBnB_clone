#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
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
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_after_save(self):
        """Test that updated_at changes after calling save."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_to_dict_type(self):
        """Test the types of values in the dictionary returned by to_dict."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict["id"], str)
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)
        self.assertEqual(bm_dict["__class__"], "BaseModel")

    def test_to_dict_missing_attributes(self):
        """Test that attributes that aren't present in the instance are not
        present in the dictionary.
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertNotIn("name", bm_dict)
        self.assertNotIn("number", bm_dict)

    def test_to_dict_with_custom_attributes(self):
        """Test the to_dict method with custom attributes."""
        bm = BaseModel(name="Alice", age=30)
        bm_dict = bm.to_dict()
        self.assertIn("name", bm_dict)
        self.assertIn("age", bm_dict)
        self.assertEqual(bm_dict["name"], "Alice")
        self.assertEqual(bm_dict["age"], 30)

    def test_updated_at_to_dict(self):
        """Test that the updated_at attribute is in the to_dict output."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIn("updated_at", bm_dict)

    def test_str_representation(self):
        """Test the __str__ representation of the BaseModel instance."""
        bm = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_str)

    def test_str_representation_custom_attributes(self):
        """Test the __str__ representation with custom attributes."""
        bm = BaseModel(name="Alice", age=30)
        expected_str = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_str)

    def test_updated_at_type(self):
        """Test that updated_at is of type datetime."""
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
