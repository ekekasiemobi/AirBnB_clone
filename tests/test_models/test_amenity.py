#!/usr/bin/python3
"""Testing amenity"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def test_name(self):
        """Test the name attribute of the Amenity class."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_to_dict(self):
        """Test the to_dict method of the Amenity class."""
        amenity = Amenity()
        amenity.name = "Pool"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Pool")
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_init(self):
        """Test the __init__ method of the Amenity class."""
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")


if __name__ == "__main__":
    unittest.main()
