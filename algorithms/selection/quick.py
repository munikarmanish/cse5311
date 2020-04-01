"""
Find the k-th smallest element in an array.
"""

import random

from ..sorting.quick import partition


def quick_select(array: list, k: int):
    """
    Find the kth-smallest element using partitioning approach (like in the
    quicksort algorithm).

    The `array` is assumed to have no duplicates.
    """
    array = list(set(array))
    return __quick_select(array, start=0, end=len(array) - 1, k=k)


def __quick_select(array, start, end, k):
    """
    Find the kth-smallest element using partitioning approach (like in the
    quicksort algorithm).

    The `array` is assumed to have no duplicates.
    """
    if k > end + 1 or k < 1:
        raise IndexError

    pivot_index = random.randint(start, end)
    pivot_index = partition(array, start, end, pivot_index)
    if pivot_index == k - 1:
        return array[pivot_index]
    if pivot_index >= k:
        return __quick_select(array, start, pivot_index - 1, k)
    return __quick_select(array, pivot_index + 1, end, k)
