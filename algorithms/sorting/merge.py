"""
Merge-sort algorithm.
"""
from copy import deepcopy


def merge_sort(array: list) -> list:
    """
    out-of-place implementation of the merge-sort sorting algorithm.
    """
    N = len(array)
    if N < 2:
        return deepcopy(array)
    mid = N // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(a: list, b: list) -> list:
    """
    Merge two sorted arrays.
    """
    a, b = deepcopy(a), deepcopy(b)
    c = []
    while a and b:
        if b[0] < a[0]:
            c.append(b.pop(0))
        else:
            c.append(a.pop(0))
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c
