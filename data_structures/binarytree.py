"""
Binary tree structure
"""


class Node:
    """
    Node of a binary tree.
    """

    def __init__(self, key: int, left: Node = None, right: Node = None):
        self.key = key
        self.left = left
        self.right = right
