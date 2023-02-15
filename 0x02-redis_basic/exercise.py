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
from typing import Union, Any, Callable
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

    def get(self, key: str, fn: Callable = None) -> Any:
        """
        get method that take a key string argument and an optional Callable
        argument named fn. This callable will be used to convert the data
        back to the desired format
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """return str"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """retrun int"""
        value = self._redis.get(key)
        return int.from_bytes(value)
