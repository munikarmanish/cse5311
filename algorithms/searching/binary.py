"""
Binary search algorithm.
"""


def __binary_search(array, start, end, key):
    """
    Returns the index of key in sorted array. Returns None if not found.
    """
    if start > end:
        return
    mid = (start + end + 1) // 2
    if key == array[mid]:
        return mid
    if key < array[mid]:
        return __binary_search(array, start, mid - 1, key)
    return __binary_search(array, mid + 1, end, key)


def binary_search(array: list, key) -> int:
    """
    Simple wrapper for __binary_search that acts on the whole list; doesn't
    require `start` and `end` arguments.
    """
    return __binary_search(array, start=0, end=len(array) - 1, key=key)
