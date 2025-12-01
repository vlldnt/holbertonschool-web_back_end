#!/usr/bin/env python3
"""Cache class REDIS"""

from typing import Union, Callable, Optional
import redis
import uuid

Types = Union[str, bytes, int, float]


class Cache():
    """Cache class Redis"""

    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Types) -> str:
        """Store data with redis cache and return UUID"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> Types:
        """Get the format and convert data into it"""
        value = self._redis.get(key)

        if value is None:
            return None
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str) -> str:
        """Get string to parametrize get() by decode from bytes"""
        return self.get(key, lambda bytes: bytes.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get int by decoding"""
        return self.get(key, int)
