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
        '''Get the fomat and convert data into it'''

        value = self._redis.get(key)

        if not value:
            return None
        if not fn:
            return value
        else:
            try:
                return fn(value)
            except Exception:
                return None

    def get_str(self, key: str) -> str:
        '''Get string to parametrize get() by decode from byytes'''
        def strfunc(bytes):
            return bytes.decode('utf-8')
        return self.get(key, strfunc)

    def get_int(self, key: str) -> int:
        '''Get int by decoding '''
        def intfunc(bytes):
            return int(bytes)
        return self.get(key, intfunc)
