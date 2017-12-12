#
# revisions.py
# @author: K4LI
#

from algopy.graphmat import *

def buildFromFile(path):
    with open(path) as file:
        directed = bool(int(file.readline()))
        order = int(file.readline())
        g = Graph(order, directed=directed) # or GraphMat
        for line in file:
            src, dst = line.strip().split(' ')
            g.addedge(int(src), int(dst))
    return g

## Exercise 1.4
### 1. Write a function that fills 2 vectors in and out that represent indegrees 
### and outdegrees of all vertices of a graph (adjacency list)

def degrees(g):
	vin = [0] * g.order
	vout = []
	for l in g.adjlists:
		vout.append(l)
		for v in l:
			vin[v] += 1
	return vin, vout

### 2. Write a function that computes the indegree and outdegree of a digraph
### (adjacency matrix)

def maxdegrees(g):
	maxin, maxout = 0, 0
	for i in range(g.order):
		tmp, tmp2 = 0, 0
		for j in range(g.order):
			tmp += g[i][j]
			tmp2 += g[j][i]
		maxin = max(maxout, tmp2)
		maxout = max(maxout, tmp)
	return maxin, maxout

## Exercise 1.5
### Returns the dot representation of a graph

# ajdacency list implementation
def todot_adj(g):
	i = 0
	for v in g.adjlists:
		for s in v:
			print(str(i) + ' --> ' + str(v))
		i += 1

######################
#	    			 #
#  	  Traversals	 #
#					 #
######################

# Exercise 2.1
## 4. BFS

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
	while !q.isempty():
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

# Exercise 2.2
### 3. DFS unidrected

# adjacency matrix
def dfs(g, src=0):
	parents = [None] * g.order
	parents[src] = -1
	_dfs(g, src, parents)
	for s in range(g.order):
		if parents[s] is None:
			parents[s] = -1
			_dfs(g, src, parents)
	return parents

def _dfs_undir(g, src, parents):
	# print(src)
	for s in g.adjlists[src]:
		if parents[s] is None:
			parents[s] = src
			_dfs_undir(g, s, parents)
		else:
			if parents[s] != s:
				print(s, '--', s, 'is a backward edge')
	# print(src)

def _dfs_dir(g, src, parents):
	pass


######################
#	    			 #
#  	  Application	 #
#					 #
######################

# Exercise 3.1
## 1. How to find a path between 2 vertices in a graph?

def path(g, src, dst):
	parents = [None] * g.order
	dist = [float('inf')] * g.order
	dist[src] = 0
	parents[src] = -1
	_dfs_path(g, src, dst, parents, dist)
	path = None
	if parents[dst] != None:
		path = [0] * (dist[dst] + 1)
		i = dist[dst]
		while parents[dst] != -1:
			path[i] = dst
			i -= 1
			dst = parents[dst]
		path[0] = src



















