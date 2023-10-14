#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.
"""
from models.engine.file_storage import FileStorage
import unittest


class FileStorageTest(unittest.TestCase):
    """REPRESENTATION  Unittests
        methods:
            test_basic_creation
            test_check_instance
            test_id_not_equal
    """
    def test_basic_creation(self):
        pass
        # obj1 = FileStorage()
        # not (self.assertIsNone(print(obj1), "test_basic_creation"))

    def test_check_instance(self):
        pass
        # obj1 = FileStorage()
        # self.assertTrue(isinstance(obj1, FileStorage), "test_check_instance")

    def test_id_not_equal(self):
        pass
        # obj1 = FileStorage()
        # obj2 = FileStorage()
        # self.assertIsNot(obj1.id, obj2.id, "must be not equal")

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))


if __name__ == "__main__":
    unittest.main()
