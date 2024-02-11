#!/usr/bin/python3
"""file storage class module unitesting"""
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os
import json


class FileStorageTest(unittest.TestCase):
    """testing filestorage"""

    def test_invalid_args(self):
        '''methods with invalid args'''
        try:
            os.remove("file.json")
        except IOError:
            pass
        with self.assertRaises(TypeError):
            FileStorage(None)
        with self.assertRaises(TypeError):
            storage.save(None)
        with self.assertRaises(TypeError):
            storage.all("storage_all")
        with self.assertRaises(AttributeError):
            storage.new("storage_new")
        with self.assertRaises(TypeError):
            storage.save("storage_save")
        with self.assertRaises(TypeError):
            storage.reload("storage_reload")

    def test_attributes(self):
        """
        testing attributes
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertFalse(hasattr(storage, '__file_path'))
        self.assertFalse(hasattr(storage, '__objects'))
        self.assertEqual(type(storage), FileStorage)

    def test_all_invalid(self):
        """Testing all method"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        file_storage_a = FileStorage()
        FileStorage._FileStorage__objects = {}
        file_storage_a.reload()
        self.assertEqual(file_storage_a.all(), {})
        self.assertEqual(dict, type(file_storage_a.all()))

    def test_new_method(self):
        """Test new method """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        f = FileStorage()
        FileStorage._FileStorage__objects = {}
        b = BaseModel()
        f.new(b)
        expected = {f"BaseModel.{b.id}": b}
        self.assertEqual(f.all(), expected)

    def test_save_method(self):
        """Test save method"""
        f = FileStorage()
        b = BaseModel()
        f.save()
        b_key = f"BaseModel.{b.id}"
        with open("file.json", "r") as file:
            file_content = json.load(file)
            self.assertTrue(file_content.get(b_key))

    def test_reload_file_not_found(self):
        """Test reload if the file does not exists"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            f = FileStorage()
            f.reload()
        except Exception:
            self.fail()

    def test_reload_file_found(self):
        """Test reload file found"""
        storage.reload()
        data = storage.all()
        self.assertNotEqual(data, {})

    def test_all_non_empty(self):
        """Test all none empty"""
        f = FileStorage()
        b = BaseModel()
        f.new(b)
        self.assertNotEqual(f.all(), {})


if __name__ == "__main__":
    unittest.main()
