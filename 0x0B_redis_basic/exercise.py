#!/usr/bin/env python3
"""Cache class REDIS"""

from typing import Union, Callable, Optional
import redis
import uuid
from functools import wraps


Types = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    '''Count number of time Cache if callabled'''

    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''Wrapper to increment redid counter before calling mehtod'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs"""

    @wraps(method)
    def wrapper(self, *args, **kwds):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache():
    """Cache class Redis"""

    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
