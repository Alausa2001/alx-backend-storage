#!/usr/bin/python3
"""
In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:).
The core of the function is very simple.
It uses the requests module to obtain
the HTML content of a particular URL and returns it.

Inside get_page track how many times a particular URL was
accessed in the key "count:{url}" and cache the
result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to
simulate a slow response and test your caching.

Bonus: implement this use case with decorators.
"""
from functools import wraps
import requests as req
import redis


redi = redis.Redis()


def count_url_access(method):

    @wraps(method)
    def count(url):
        url_key = url
        count_key = 'count:{}'.format(url)
        redi.incr(count_key, amount=1)
        html = method(url)
        redi.set(url_key, html)
        redi.expire(url, 10)
        return html
    return count


@count_url_access
def get_page(url: str) -> str:
    """requests a url and returns the HTML content"""
    html = req.get(url)
    return html.text
