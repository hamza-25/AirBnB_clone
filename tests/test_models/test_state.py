#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
from models.state import State
import unittest


class StateTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        obj1 = State()
        not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        obj1 = State()
        self.assertTrue(isinstance(obj1, State), "test_check_instance")

    def test_id_not_equal(self):
        obj1 = State()
        obj2 = State()
        self.assertIsNot(obj1.id, obj2.id, "must be not equal")


if __name__ == "__main__":
    unittest.main()
