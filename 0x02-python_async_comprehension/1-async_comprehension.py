#!/usr/bin/env python3
"""Retrieve the async_generator module from the preceding assignment and proceed to create a coroutine named async_comprehension, which requires no parameters. This coroutine is designed to gather 10 random numbers through an asynchronous comprehension using async_generator. Subsequently, it should deliver the set of 10 randomly generated numbers..
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
