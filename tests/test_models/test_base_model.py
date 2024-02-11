#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """
    Testng BaseModel
    """

    def test_attributes(self):
        """
        test_attributes
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_id_generation(self):
        """
        testing id generating
        """
        base_model_a = BaseModel()
        base_model_b = BaseModel()
        self.assertNotEqual(base_model_a.id, base_model_b.id)

    def test_str_representation(self):
        """
        testing string representation
        """
        base_model = BaseModel()
        expected = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected)

    def test_save_method(self):
        """
        testing save() method
        """
        clone_base_model = BaseModel()
        original_updated_at = clone_base_model.updated_at
        clone_base_model.save()
        self.assertNotEqual(original_updated_at, clone_base_model.updated_at)

    def test_to_dict_method(self):
        """
        testing to_dict method
        """
        test_base_model = BaseModel()
        expected_dict = {
            'id': test_base_model.id,
            'created_at': test_base_model.created_at.isoformat(),
            'updated_at': test_base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(test_base_model.to_dict(), expected_dict)

    def test_initialization_with_arguments(self):
        """
        testing initialization with arguments aka kgwars
        """
        data = {
            'id': 'some_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T13:00:00.000000'
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, data['id'])
        self.assertEqual(base_model.created_at, datetime.strptime(
            data['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.updated_at, datetime.strptime(
            data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))

    def test_case_empty_arguments(self):
        """
        testing case empty arguments
        """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_edge_case_invalid_datetime_format(self):
        """
        testing invalid datetime format
        """
        data = {
            'id': 'some_id',
            'created_at': '2022-01-01 12:00:00',
            'updated_at': '2022-01-01 13:00:00'
        }
        with self.assertRaises(ValueError):
            BaseModel(**data)

    def test_save_to_json_file(self):
        """ testing saving method """
        base_model = BaseModel()
        base_model.save()
        with open("file.json", "r") as file:
            self.assertIn(f"BaseModel.{base_model.id}", file.read())


if __name__ == '__main__':
    unittest.main()
