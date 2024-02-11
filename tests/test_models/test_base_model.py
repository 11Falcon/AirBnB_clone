#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os
import models
from time import sleep


class TestBaseModel_initiation(unittest.TestCase):
    """
    Testing the initiation of our BaseModel class
    """

    def test_no_args(self):
        """ testing when no args are initating"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_and_string(self):
        """is the id a public string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_and_datetime(self):
        """ is created_at public and with type datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_and_datetime(self):
        """ is updated_at public and with type datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

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

    def test_created_at_of_two_instances(self):
        """ two BaseModel created in different time"""
        falcon1 = BaseModel()
        sleep(1)
        falcon2 = BaseModel()
        self.assertLess(falcon1.created_at, falcon2.created_at)

    def test_updated_at_of_two_instances(self):
        """two BaseModel created in different time"""
        falcon1 = BaseModel()
        sleep(1)
        falcon2 = BaseModel()
        self.assertLess(falcon1.updated_at, falcon2.updated_at)

    def test_str_representation(self):
        """
        testing string representation
        """
        base_model = BaseModel()
        expected = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected)

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        falcon = BaseModel(id ="11", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(falcon.id, "11")
        self.assertEqual(falcon.created_at, date)
        self.assertEqual(falcon.updated_at, date)

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
            'created_at': '2024-08-06T12:00:00.000000',
            'updated_at': '2024-08-06T13:00:00.000000'
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

    def test_docs(self):
        """ everything is documented """

        self.assertIsNotNone(models.base_model.__doc__)


if __name__ == '__main__':
    unittest.main()
