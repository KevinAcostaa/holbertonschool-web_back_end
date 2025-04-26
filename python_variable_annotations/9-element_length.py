from typing import Iterable, Tuple, List, Any


def element_length(lst: Iterable[Any]) -> List[Tuple[Any, int]]:
    return [(i, len(i)) for i in lst]
