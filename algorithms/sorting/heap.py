"""
Heap-sort sorting algorithm.
"""
from copy import deepcopy

from data_structures.heap import build_min_heap, min_heap_pop


def heap_sort(array: list) -> list:
    """
    Out-of-place implementation of the heap-sort sorting algorithm.
    """
    heap = build_min_heap(deepcopy(array))
    return [min_heap_pop(heap) for i in range(len(array))]
