#!/usr/bin/python3
''' file storage mod '''
import json
from models.base_model import BaseModel

class_model = {"BaseModel": BaseModel}

class FileStorage(object):
    """FILE storage engine.

    Attributes:
        __file_path (string): path of the file to save objects in
        __objects (dictionary): A dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dic of the class
        '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __object
            with the key <class name>.<id>
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' saves the object to a JSON '''
        new_object = {}
        for key in FileStorage.__objects:
            new_object[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_object, file)

    def reload(self):
        ''' Reloads an object from a JSON '''
        try:
            with open(self.__file_path, 'r') as file:
                file_data = json.load(file)
                for key, value in file_data.items():
                    oop = class_model[value["__class__"]](**value)
                    FileStorage.__objects[key] = oop
        except FileNotFoundError:
            pass
