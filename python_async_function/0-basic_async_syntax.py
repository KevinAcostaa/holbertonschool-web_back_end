#!/usr/bin/env python3
"""
this module contains a function
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    this function return number random
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
