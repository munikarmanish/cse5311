"""
Binary min/max heap data structure.
"""


def min_heapify(array: list, index: int):
    """
    Push the given root down to its proper place.
    """
    left = 2 * index + 1
    right = left + 1
    smallest = index

    if left < len(array) and array[left] < array[smallest]:
        smallest = left

    if right < len(array) and array[right] < array[smallest]:
        smallest = right

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest)


def max_heapify(array: list, index: int):
    """
    Push the given root down to its proper place.
    """
    left = 2 * index + 1
    right = left + 1
    largest = index

    if left < len(array) and array[left] > array[largest]:
        largest = left

    if right < len(array) and array[right] > array[largest]:
        largest = right

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        max_heapify(array, largest)


def build_min_heap(array: list) -> list:
    """
    Build a min-heap from an existing array.
    """
    # all non-leaf nodes (bottom-up)
    for i in range(len(array) // 2, -1, -1):
        min_heapify(array, i)

    return array


def build_max_heap(array: list) -> list:
    """
    Build a max-heap from an existing array.
    """
    # all non-leaf nodes (bottom-up)
    for i in range(len(array) // 2, -1, -1):
        max_heapify(array, i)

    return array


def min_heap_push(array: list, key: int):
    """
    Push an item to heap.
    """
    index = len(array)
    array.append(key)
    while index > 0:
        parent = (index - 1) // 2
        if array[index] >= array[parent]:
            break
        array[index], array[parent] = array[parent], array[index]
        index = parent


def min_heap_pop(array: list) -> int:
    """
    Pop out the root of heap (min element).
    """
    # item to return
    out = array[0]
    last_item = array.pop(-1)
    if array:
        array[0] = last_item
        min_heapify(array, 0)
    return out


def max_heap_push(array: list, key: int):
    """
    Push an item to heap.
    """
    index = len(array)
    array.append(key)
    while index > 0:
        parent = (index - 1) // 2
        if array[index] <= array[parent]:
            break
        array[index], array[parent] = array[parent], array[index]
        index = parent


def max_heap_pop(array: list) -> int:
    """
    Pop out the root of heap (max element).
    """
    # item to return
    out = array[0]
    last_item = array.pop(-1)
    if array:
        array[0] = last_item
        max_heapify(array, 0)
    return out
