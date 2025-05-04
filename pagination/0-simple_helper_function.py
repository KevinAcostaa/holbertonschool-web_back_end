#!/usr/bin/env python3
"""
this module contains a function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    return tuple
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
