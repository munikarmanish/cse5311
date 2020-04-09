"""
Implementation of the Prim's algorithm to find the minimum spanning tree
(MST) of a graph.
"""

from data_structures.heap import Heap


def prim(G, root=None):
    """
    Find the minimim spanning tree of a graph using Prim's algorithm. If root
    is given, use it as the starting node.
    """
    nodes = Heap([(float("inf"), n) for n in G.nodes])
    parent = {n: None for n in G.nodes}
    if root:
        nodes[root] = 0
    mst = set()
    while nodes:
        node = nodes.pop()[0]
        if parent[node] is not None:
            mst.add((parent[node], node))
        for neigh, weight in G[node].items():
            if neigh in nodes and weight < nodes[neigh]:
                nodes[neigh] = weight
                parent[neigh] = node
    return mst
