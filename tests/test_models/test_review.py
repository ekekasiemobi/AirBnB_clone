#!/usr/bin/python3
"""This test module defines tests for review.py"""

import unittest
from models.review import Review  # Import the Review class
from models.base_model import BaseModel  # Import the BaseModel class
from models import storage


class TestReview(unittest.TestCase):
    """Test cases for review class"""
    
    def setUp(self):
        """Create an instance of Review before each test method"""
        self.review = Review()
    
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_attribute_initialization(self):
        """test initialization of attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
    
    def test_place_id_attr(self):
        """Test Review has attr place_id, and it's an empty string"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")

    def test_attribute_values(self):
        """test if the values set correctly"""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "5 star!"

        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "5 star!")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

    def test_update_attribute_values(self):
        """test if values update correctly"""
        self.review.place_id = "133"
        self.review.user_id = "466"
        self.review.text = "5 star! Beautiful home"

        self.assertEqual(self.review.place_id, "133")
        self.assertEqual(self.review.user_id, "466")
        self.assertEqual(self.review.text, "5 star! Beautiful home")

if __name__ == '__main__':
    unittest.main()

