#!/usr/bin/env python3
"""
function that takes a float as an argument and returns
a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that takes a float as an argument and returns
    a function that multiplies a float by multiplier
    """
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
