#!/usr/bin/python3
"""Defines unittests for models/user.py.
"""
from models.user import User
import unittest


class UserTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = User()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = User()
        self.assertTrue(isinstance(obj1, User), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = User()
        obj2 = User()
        self.assertIsNot(obj1.id, obj2.id, "must be not equal")


if __name__ == "__main__":
    unittest.main()
