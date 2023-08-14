#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity__to__dict
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""
    def test_attributes_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_name_attr(self):
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_attribute_types(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_attribute_values(self):
        city = City()
        city.state_id = "234"
        city.name = "Nigeria"
        self.assertEqual(city.state_id, "234")
        self.assertEqual(city.name, "Nigeria")

    def test_update_attribute_values(self):
        city = City()
        city.name = "Enugu"
        self.assertEqual(city.name, "Enugu")

    def test_is_subclass(self):
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))


if __name__ == '__main__':
    unittest.main()
