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

## DFS

*Think recursively*  

# Appendix

![graph](https://image.noelshack.com/fichiers/2017/50/1/1513003916-tuto-graph22.png)
![digraph](https://image.noelshack.com/fichiers/2017/50/1/1513003917-tuto-digraph12.png)