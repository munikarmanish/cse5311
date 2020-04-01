"""
Bubble sort algorithm.
"""


def bubble_sort(array: list) -> list:
    """
    In-place implementation of bubble-sort sorting algorithm.

    Pseudocode:

        for every element:
            bubble it up
    """
    N = len(array)

    for i in range(N):
        # last i elements are sorted

        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
