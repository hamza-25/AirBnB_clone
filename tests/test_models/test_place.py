#!/usr/bin/python3
"""Defines unittests for models/place.py.
"""
from models.place import Place
import unittest


class PlaceTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = Place()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = Place()
        self.assertTrue(isinstance(obj1, Place), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = Place()
        obj2 = Place()
        self.assertIsNot(obj1.id, obj2.id, "must be not equal")


if __name__ == "__main__":
    unittest.main()
