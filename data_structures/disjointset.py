"""
Implementation of the "disjoint set" data structure.
"""

from collections import defaultdict


class DisjointSet:
    """
    Disjoint set of items.
    """

    def __init__(self, items=None, parents=None):
        self.items = [] if items is None else items
        self.parents = parents
        if parents is None:
            self.parents = {item: None for item in items}

    def find(self, item):
        """
        Find the set representative.
        """
        if self.parents[item] is None:
            return item
        return self.find(self.parents[item])

    def union(self, a, b):
        """
        Merge two sets (if not already merged).
        """
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            self.parents[b_root] = a_root

    def __repr__(self):
        sets = defaultdict(set)
        for item in self.items:
            root = self.find(item)
            sets[root].add(item)
        return repr(list(sets.values()))
