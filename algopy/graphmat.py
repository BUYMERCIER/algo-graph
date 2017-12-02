# -*- coding: utf-8 -*-
"""Graph module.

Provide an implementation of graphs with adjacency matrix.
This can also be called static implementation.

In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. The vertex key, or number, can then be used to access its
neighbour list.

"""

#
class GraphMat:
    """ Simple class for static graph.

    Attributes:
        order (int): Number of vertices.
        directed (bool): True if the graph is directed. False otherwise.
        adj (List[List[int]]): Adjacency matrix
    """

    def __init__(self, order, directed=False):
        """
        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.
        """
 
        self.order = order
        self.directed = directed
        self.adj = [[0 for j in range(order)] for i in range(order)]

    def addedge(self, src, dst):
        if src < 0 or src >= self.order:
            raise IndexError("invalid src index")
        if dst < 0 or dst >= self.order:
            raise IndexError("invalid dst index")
        self.adj[src][dst] += 1
        if not self.directed and src != dst:
            self.adj[dst][src] += 1

# 
class Graph:
    """ Simple class for graph: adjacency lists

    Attributes:
        order (int): Number of vertices.
        directed (bool): True if the graph is directed. False otherwise.
        adjlists (List[List[int]]): Lists of connected vertices for each vertex.

    """

    def __init__(self, order, directed=False):
        """Init graph, allocate adjacency lists

        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.

        """

        self.order = order
        self.directed = directed
        self.adjlists = []
        for _ in range(order):
            self.adjlists.append([])

    def addedge(self, src, dst):
        if src < 0 or src >= self.order:
            raise IndexError("invalid src index")
        if dst < 0 or dst >= self.order:
            raise IndexError("invalid dst index")
        self.adjlists[src].append(dst)
        if not self.directed and src != dst:
            self.adjlists[dst].append(src)

