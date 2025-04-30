#!/usr/bin/env python3
"""
this module contains a function
"""


import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    this function sorts the contents of a list of floats
    """
    list_float = []

    for i in range(n):
        list_float.append(task_wait_n(max_delay))
    m = await asyncio.gather(*list_float)
    return sorted(m)
