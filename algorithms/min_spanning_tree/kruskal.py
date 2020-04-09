"""
Kruskal's algorithm for minimum spanning tree.
"""

from data_structures.disjointset import DisjointSet
from data_structures.heap import build_min_heap, min_heap_pop


def kruskal(G):
    """
    Find the minimim spanning tree of the given graph using Kruskal's algorithm.
    """
    selected_edges = set()
    ds = DisjointSet(G.nodes)
    edges = build_min_heap([(w, (u, v)) for u, v, w in G.edges])
    while edges:
        (u, v) = min_heap_pop(edges)[1]
        u_root, v_root = ds.find(u), ds.find(v)
        if u_root != v_root:
            selected_edges.add((u, v))
            ds.union(u_root, v_root)
    return selected_edges
