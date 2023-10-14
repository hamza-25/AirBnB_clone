#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
"""
from models.base_model import BaseModel
import unittest


class BaseModelTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = BaseModel()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = BaseModel()
        self.assertTrue(isinstance(obj1, BaseModel), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertIsNot(obj1.id, obj2.id, "must be not equal")


if __name__ == "__main__":
    unittest.main()
