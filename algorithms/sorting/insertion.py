"""
Insertion sort algorithm.
"""


def insertion_sort(array: list) -> list:
    """
    In-place implementation of insertion-sort algorithm.

    Pseudocode:
        for every element from left to right:
            while left > self:
                move left
    """
    N = len(array)

    for i in range(1, N):
        # find the position for array[i] in the left/sorted part
        j = i - 1
        while j >= 0 and array[j + 1] < array[j]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1

    return array
