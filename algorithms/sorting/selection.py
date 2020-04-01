"""
Selection sort algorithm.
"""


def selection_sort(array: list) -> list:
    """
    In-place implementation of the selection-sort algorithm.

    Pseudocode:
        1. find the min item, move it to first
        2. repeat #1 by excluding the first item
    """
    N = len(array)

    # i is the number of items in the left/sorted part
    for i in range(N):

        # get the index of min item from the right/unsorted part
        i_min = i
        for j in range(i + 1, N):
            if array[j] < array[i_min]:
                i_min = j

        # swap the min item with the first item of the unsorted/right part
        array[i], array[i_min] = array[i_min], array[i]

    return array
