# Recap

A graph is a non-linear data structure.  
It is a set of vertices (aka nodes) and a set of edges. **G = (v,e)**

Two main types of graphs:  
- directed graph (digraph)
- undirected graph

They can be weighted (a cost on every node).

### Properties:

Self-loop (edge with same start and end points)  
Multiedge (several edges from a vertex to another)  

*if there are no self-loops or multiedges, it's called a simple graph*

In a directed graph, the maximum number of edges is ```n * (n - 1)``` (n being the number of vertices). This is true if it is a simple graph.  
In an undirected graph, the max number of edges is ```n * (n - 1) / 2```  


*Dense graph -> adjacency matrix*  
*Spares graph -> adjacency list*  

### Paths

A walk (or path) is a sequence of vertices where each adjacent pair is connected by and edge.  
A simple (elementary) path is a walk where no vertices are repeated.  

**Strongly connected**: if there is a path from any vertex to any other vertex.

A cycle starts and ends at the same vertex and no edge/vertex is repeated.  
A graph with no cycle is called **acyclic**

# Implementations

## Adjacency list

Good on memory, but bad on computation time.  

![Example](http://btechsmartclass.com/DS/images/Graph%20Adjacency%20List.jpg)

### Python implementation

```python
class Graph:
    """ Simple class for graph: adjacency lists
    """

    def __init__(self, order, directed=False):
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
```  

We have a graph **g**.  

**g.order** (the order of the graph - the number of vertices)  
**g.directed** (boolean: True if directed False if undirected)  
**g.adjlists** (a list of lists - index 0 is the list if outgoing links from 0 to the elements of the list)

Attributes:
* order (int): Number of vertices.
* directed (bool): True if the graph is directed. False otherwise.
* adjlists (List[List[int]]): Lists of connected vertices for each vertex.

## Adjacency matrix

We can store the graph in a ```v * v``` matrix (where v is the number of vertices of the graph).  
Good on computation time, but bad on memory.
  
![Example](http://btechsmartclass.com/DS/images/Graph%20Adjacency%20Matrix%201.jpg)

For an undirected graph, this matrix is symmetric.  

### Python implementation

```python
class GraphMat:
    """ Simple class for static graph.
    """

    def __init__(self, order, directed=False): 
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
```

We have a graph **g**.

**g.order** (the order of the graph - the number of vertices)  
**g.directed** (boolean: True if directed False if undirected)  
**g.adj** () 

# Traversals

## BFS 

*BFS -> think about queues*  

```python
from algopy.queues import *

# hat function
def bfs(g, src=0):
    parents = [None] * g.order
    parents[src] = -
    _bfs(g, src, parents) # the actual BFS
    for v in range(g.order):
        if parents[v] is None:
            parents[v] = -1
            _bfs(g, v, parents)
    return parents

# ajacency list
def _bfs(g, src, parents):
    q = Queue()
    q.enqueue(src)
    while not q.isempty():
        cur = q.dequeue
        for s in g.adjlists[cur]:
            if parents[s] is None:
                parents[s] = cur
                q.enqueue(s)

# adjacency matrix
def _bfs_mat(g, src, parents):
    q = Queue()
    q.enqueue(src)
    while not q.isempty():
        cur = q.dequeue()
        #for succ in g.adjlists[cur]:
        for succ in range(g.order):
            if g.adj[cur][succ]:
                if parents[succ] is None:
                    parents[succ] = cur
                    q.enqueue(succ)
```

## DFS

*Think recursively*  

### Preorder and postorder properties

An edge u->v is:
- discovery if: pre[u] < pre[v] < post[v] < post[u]
- forward if: pre[u] < pre[v] < post[v] < post[u]
- backward if: pre[v] < pre[u] < post[u] < post[v]
- cross if: pre[v] < post[v] < pre[u] < post[u]

## How to represent spanning forests

### Static case

- DFS
- BFS
- Transitive closure

### Evolutive case

- Parents list
- Union by rank
- Path compression

# Appendix

![graph](https://image.noelshack.com/fichiers/2017/50/1/1513003916-tuto-graph22.png)
![digraph](https://image.noelshack.com/fichiers/2017/50/1/1513003917-tuto-digraph12.png)
