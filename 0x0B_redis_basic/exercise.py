#!/usr/bin/env python3
"""Cache class REDIS"""

from typing import Any
import redis
import uuid


class Cache():
    """Cache class Redis"""

    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Store data with redis cache adn return UUID"""
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
