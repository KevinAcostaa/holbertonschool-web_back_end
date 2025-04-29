#!/usr/bin/env python3
"""
this module contains a function
"""


import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n



async def measure_time(n: int, max_delay: int) -> float:
    """
    this function calculate time
    """
    start_time = time.time()
    await (wait_n(n, max_delay))
    end_time = time.time()
    all_time = (end_time - start_time) / n
    return all_time
