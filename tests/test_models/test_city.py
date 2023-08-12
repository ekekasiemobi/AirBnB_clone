#!/usr/bin/python3
"""Test module defines tests for city.py"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """test cases for the city class"""
    def test_attributes_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_attribute_types(self):
        """test for correct attribut types"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_attribute_values(self):
        """ set values for attributes """
        self.city.state_id = "123"
        self.city.name = "Nairobi"

        self.assertEqual(self.city.state_id, "123")
        self.assertEqual(self.city.name, "Nairobi")

    def test_update_attribute_values(self):
        """ update values of city """
        self.city.name = "Mombasa"

        self.assertEqual(self.city.name, "Mombasa")

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

if __name__ == '__main__':
    unittest.main()
