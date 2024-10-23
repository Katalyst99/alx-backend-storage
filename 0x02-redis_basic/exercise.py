#!/usr/bin/env python3
"""
The module for how to use redis for basic operations and as a simple cache.
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A decorator that takes a single argument and returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A function decorator when defining a wrapper function."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """A decorator that takes a single argument and returns a Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """A function decorator when defining a wrapper function."""
        inputKey = f"{method.__qualname__}:inputs"
        self._redis.rpush(inputKey, str(args))
        outputKey = f"{method.__qualname__}:outputs"
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputKey, output)
        return output
    return wrapper


class Cache:
    """The class Cache"""
    def __init__(self):
        """Inits an instance of Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data argument and returns a string."""
        randomKey = str(uuid4())
        self._redis.set(randomKey, data)
        return randomKey

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None,
            ) -> Union[str, bytes, int, float]:
        """
        Method that take a key string argument and,
        an optional Callable argument named fn
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """Method that will automatically parametrize Cache.get (str)"""
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Method that will automatically parametrize Cache.get (int)"""
        return self.get(key, lambda i: int(i))
