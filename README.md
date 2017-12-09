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

```python
class Graph
```  

We have a graph **g**.  

**g.order** (the order of the graph - the number of vertices)  
**g.directed** (boolean: True if directed False if undirected)  
**g.adjlists** (a list of lists - index 0 is the list if outgoing links from 0 to the elements of the list)

## Adjacency matrix

We can store the graph in a ```v * v``` matrix (where v is the number of vertices of the graph).  
![Example](http://btechsmartclass.com/DS/images/Graph%20Adjacency%20Matrix%201.jpg)

```python
class GraphMat
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

