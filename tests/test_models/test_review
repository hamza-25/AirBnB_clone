#!/usr/bin/python3
"""Defines unittests for models/review.py.
"""
from models.review import Review
import unittest


class ReviewTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = Review()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = Review()
        self.assertTrue(isinstance(obj1, Review), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = Review()
        obj2 = Review()
        self.assertIsNot(obj1.id, obj2.id, "must be not equal")


if __name__ == "__main__":
    unittest.main()
