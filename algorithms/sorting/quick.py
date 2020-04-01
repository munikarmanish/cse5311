"""
Quick-sort sorting algorithm (random-pivot).
"""

import random


def quick_sort(array: list, start: int = 0, end: int = None) -> list:
    """
    In-place implementation of the quick-sort sorting algorithm.
    """
    # if end is not given, set it as the last index of array
    end = len(array) - 1 if end is None else end

    if start < end:
        pivot_index = random.randint(start, end)
        pivot_index = partition(array, start, end, pivot_index)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)
    return array


def partition(array: list, start: int, end: int, pivot_index: int):
    """
    Partition the array and return the pivot index.
    """
    # swap pivot with the last item
    pivot = array[pivot_index]
    array[end], array[pivot_index] = array[pivot_index], array[end]

    i = start  # pointer to start of bigger elements
    for j in range(start, end):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[end] = array[end], array[i]
    return i
