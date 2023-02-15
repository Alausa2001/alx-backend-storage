#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the
Redis client as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string.
The method should generate a random key (e.g. using uuid), store the
input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a
str, bytes, int or float.
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """cache class"""
    def __init__(self):
        """instance intialization"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a rndom key and then uses this key to
        store the data argument into redis database
        """
        self.key = str(uuid4())
        self._redis.set(self.key, data)
        return self.key
