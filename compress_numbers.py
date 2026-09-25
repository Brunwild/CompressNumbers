from typing import Iterable, List


def compress_numbers(numbers: Iterable) -> List:    
    result: List = []
    for value in numbers:
        if not result or result[-1] != value:
            result.append(value)
    return result
