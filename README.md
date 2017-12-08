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

In a directed graph, the maximum number of edges is ```n * (n - 1)``` (n being the number of vertices)

# Implementations

## Graph (adjlists)

```
class Graph
```  

We have a graph **g**.  

**g.order** (the order of the graph - the number of vertices)  
**g.directed** (boolean: True if directed False if undirected)  
**g.adjlists** (a list of lists - index 0 is the list if outgoing links from 0 to the elements of the list)

## GraphMat

```
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

