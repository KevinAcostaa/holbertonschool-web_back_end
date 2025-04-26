#!/usr/bin/env python3
"""
function parameters and return values with the appropriate types
"""
from typing import Iterable, Tuple, List, Any


def element_length(lst: Iterable[Any]) -> List[Tuple[Any, int]]:
    """
    function parameters and return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
