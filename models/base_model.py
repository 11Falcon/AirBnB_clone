#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

class BaseModel():
    '''Base Class Mod'''
    def __init__(self, *args, **kwargs):
        """initializing"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, timeformat)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """[<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save(self): updates the public instance attribute with the current datetime using now()"""
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        """returns dictionary containing all keys/values of __dict__ of the instance plus class"""
        dictionnary = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dictionnary[key] = value.isoformat()
            else:
                dictionnary[key] = value
        dictionnary["__class__"] = self.__class__.__name__
        return dictionnary
