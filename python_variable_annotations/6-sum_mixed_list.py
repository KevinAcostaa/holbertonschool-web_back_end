#!/usr/bin/env python3
"""
Function that receives a list of integers and float as a parameter
and returns the float sum
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that receives a list of integers and float as a parameter
    and returns the float sum
    """
    return sum(mxd_lst)
