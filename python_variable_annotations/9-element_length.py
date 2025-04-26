#!/usr/bin/env python3
"""
function parameters and return values with the appropriate types
"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function parameters and return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
