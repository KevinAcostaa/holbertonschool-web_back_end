#!/usr/bin/env python3
"""
this module contains a function
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    return a list of 10 num random
    """
    return [i async for i in async_generator()]
