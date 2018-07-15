"""module for hash utils"""
import hashlib
import os
import base64
import uuid


class HashUtils(object):
    def __init__(self, arg):
        """Constructor of HashUtils objects"""
        self.arg = arg
        self.hash_cache = None
        self._salt = None

    def __hash__(self):
        """overwirte hash method"""
        if self.hash_cache is None:
            self.hash_cache = abs(hash(self.arg+self.salt))
        return self.hash_cache

    @property
    def salt(self):
        """method for salt generation"""
        if self._salt is None:
            self._salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
            return self._salt
        else:
            return self._salt

    @salt.setter
    def salt(self, x):
        """Setter used only for testing"""
        if x < 0:
            self._salt = str(0)
        elif x > 1000:
            self._salt = str(1000)
        else:
            self._salt = str(x)
