#!/usr/bin/python3
"""Test defines tests for user.py"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Create an instance of User"""
        self.user = User()

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_attribute_initialization(self):
        """Test initialization of attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attributes(self):
        """test attribute setup"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_creation(self):
        """set values for attributes"""
        user = User(email="user@example.com", password="password",
                    first_name="Felix", last_name="Charles")
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "Felix")
        self.assertEqual(user.last_name, "Charles")

    def test_email_attr(self):
        """Test User has attr email"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_password_attr(self):
        """Test User has attr password"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_first_name_attr(self):
        """Test User has attr first_name"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attr(self):
        """Test User has attr last_name"""
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
