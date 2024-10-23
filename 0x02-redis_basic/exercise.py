#!/usr/bin/env python3
"""
The module for how to use redis for basic operations and as a simple cache.
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """The class Cache"""
    def __init__(self):
        """Inits an instance of Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data argument and returns a string."""
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey
