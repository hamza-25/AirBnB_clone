#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
"""
from models.amenity import Amenity
import unittest


class AmenityTestModel(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = Amenity()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = Amenity()
        self.assertTrue(isinstance(obj1, Amenity), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = Amenity()
        obj1.name = "amenity"
        obj2 = Amenity()
        obj2.name = "amenityClass"
        self.assertIsNot(obj1.name, obj2.name, "must be not equal")


if __name__ == "__main__":
    unittest.main()
