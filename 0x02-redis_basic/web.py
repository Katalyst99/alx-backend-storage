#!/usr/bin/env python3
"""The module for implementing an expiring web cache and tracker"""
import redis
import requests
from typing import Callable
from functools import wraps

redIs = redis.Redis()


def url_count(method: Callable) -> Callable:
    """A decorator takes a single argument and returns a Callable"""
    @wraps(method)
    def wrapper(url):
        cachedOutput = redIs.get(f"cached:{url}")
        if cachedOutput:
            return cachedOutput.decode('utf-8')

        output = method(url)

        redIs.incr(f"count:{url}")
        redIs.setex(f'cached:{url}', 10, output)
        return output
    return wrapper


@url_count
def get_page(url: str) -> str:
    """
    Uses the requests module to obtain the HTML content of a particular URL,
    and returns it.
    """
    return requests.get(url).text
