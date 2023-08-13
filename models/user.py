#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__
        and the class name in '__class__' key.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
