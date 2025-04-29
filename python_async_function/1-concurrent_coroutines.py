#!/usr/bin/env python3
"""
this module contains a function
"""


import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    this function sorts the contents of a list of floats
    """
    list_float = []

    for i in range(n):
        list_float.append(wait_random(max_delay))
    m = await asyncio.gather(*list_float)
    return sorted(m)
