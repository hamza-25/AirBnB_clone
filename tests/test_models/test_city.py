#!/usr/bin/python3
"""Defines unittests for models/city.py.
"""
from models.city import City
import unittest


class CityTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = City()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = City()
        self.assertTrue(isinstance(obj1, City), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = City()
        obj2 = City()
        self.assertIsNot(obj1.id, obj2.id, "must be not equal")


if __name__ == "__main__":
    unittest.main()
