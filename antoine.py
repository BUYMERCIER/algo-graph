from algopy.queue import Queue

# Graphs - Implementation and traversals

class GraphMat:
    def __init__(self, order, directed=False):
        self.order = order
        self.directed = directed
        self.adj = [[o for j in range(order)] for i in range(order)]

def __bfs(g, src, parents):
    q = Queue()
    q.enqueue(src)
    while not q.isempty():
        cur = q.dequeue()
        for succ in g.adjlists[cur]:
            if parents[succ] is None:
                parents[succ] = cur
                q.enqueue(succ)

def __bfs_mat(g, src, parents):
    q = Queue()
    q.enqueue(src)
    while not q.isempty():
        cur = q.dequeue()
        # For succ in g.adjlists[cur]
        for succ in range(g.order):
            if g.adj[cur][succ]:
                if parents[succ] is None:
                    parents[succ] = cur
                    q.enqueue(succ)

def breadth_first_full_traversal(g, src=0):
    parents = [None] * g.order
    parents[src] = -1
    __bfs(g, src, parents)
    for v in range(g.order):
        if parents[v] is None:
            parents[v] = -1
            __bfs(g, v, parents)
    return parents

def bfs_all_options(g, src=None, full=True, traversal=__bfs):
    if src in None and not full:
        raise Exception("Can't do that")
    parents = [None] * g.order
    if src != None:
        parents[src] = -1
        traversal(g, src, parents)
    if full:
        for v in range(g.order):
            if parents[v] is None:
                parents[v] = -1
                traversal(g, v, parents)
    return parents

def __dfs_undir(g, v, parents):
    for s in g.adjlists[v]:
        if parents[s] is None:
            parents[s] = v
            __dfs_undir(g, s, parents)
        else:
            if parents[v] != s:
                print(v, '--', s, 'is a backward edge')

import graphviz

def parents_to_forest(parents, src=0):
    forest = graphviz.Digraph()
    forest.node(str(src))
    for v in range(len(parents)):
        if parents[v] == -1:
            forest.node(str(v))
        else:
            forest.edge(str(parents[v]),str(v))
    return forest

"""
Let pre and post be vectors containing pre-order and post-order of encounter for
each vertex.

And edge u -> v is:

* a discovery edge if: pre[u] < pre[v] < post[v] < post[u]
* a forward edge if: pre[u] < pre[v] < post[v] < post[u]
* a backward edge if: pre[v] < pre[u] < post[u] < post[v]
* a cross edge if: pre[v] < post[v] < pre[u] < post[u]
"""

def __dfs_dir(g, u, parents, pre, post, count):
    count += 1
    pre[u] = count
    for v in g.adjlists[u]:
        if parents[v] is None:
            parents[v] = u
            count = __dfs_dir(g, v, parents, pre, post, count)
        else:
            kind = ''
            if post[v] is None:
                kind = 'backward'
            elif pre[u] < pre[v]:
                kind = 'forward'
            else:
                kind = 'cross'
            print('{}->{}: {} edge'.format(u, v, kind))
    count += 1
    post[u] = count
    return count

def dfs_dir_extra_edges(g, src=0):
    parents, pre, post = [None] * g.order, [None] * g.order, [None] * g.order
    count = 0
    parents[src] = -1
    count = __dfs_dir(g, src, parents, pre, post, count)
    for u in range(g.order):
        if parents[u] is None:
            parents[u] = -1
            count = __dfs_dir(g, u, parents, pre, post, count)
    return parents, pre, post, count

def __bfs_path(g, src, dst, parents, dist):
    g = Queue()
    q.enqueue(src)
    while not q.isempty():
        cur = q.dequeue()
        for succ in g.adjlists[cur]:
            if parents[succ] is None:
                parents[succ] = cur
                dist[succ] = dist[cur] + 1
                if succ == dst:
                    return
                q.enqueue(succ)

def find_path(g, src, dst):
    parents = [None] * g.order
    dist = [float('infinity')] * g.order
    dist[src] = 0
    parents[src] = -1
    __bfs_path(g, src, dst, parents, dist)
    path = None
    if parents[dst] != None:
        path = [0] * (dist[dst] + 1)
        i = dist[dst]
        while parents[dst] != -1:
            path[i] = dst
            i -= 1
            dst = parents[dst]
        path[0] = src
    return parents, dist, path

#   3.2 Distance from start

# Distance 1 of 2, 3, 4, 7
# Distance 2 of 5, 6, 10
# Distance 3 of 9, 8, 11

def dist_from_start(G, src, dmin, dmax):
    parents = [None] * G.order
    dist = 0
    res = []
    q = Queue()
    q.enqueue(src)
    q.enqueue(None)
    parents[src] = -1
    while not q.isempty():
        cur = q.dequeue()
        if cur is None:
            if q.isempty():
                return res
            q.enqueue(None):
            dist += 1
        else:
            if dist < dmax:
                for succ in range(g.order):
                    if G.adj[cur][succ]:
                        if parents[succ] is None:
                            parents[succ] = curr
                            q.enqueue(succ)
                            if dist >= dmin - 1:
                                res.append(succ)

#   Exercise 3.2 CORRECTION

def distance(g, src, dmin, dmax):
    dist = [None] * g.order
    q = Queue()
    q.enqueue(src)
    dist[src] = 0
    last = 0
    if dmin == 0:
        print(src)
    while not q.isempty():
        cur = q.dequeue()
        if dist[cur] >= dmin and dist[cur] != last:
            print()
        last = dist[cur]
        if dist[cur] >= dmin - 1:
            for s in range(g.order):
                if g.adj[cur][s] and dist[dist] is None:
                    print(s, end=' ')
        if dist[cur] < dmax - 1:
            for s in range(g.order):
                if g.adj[cur][s] and dist[s] is None:
                    dist[s] = dist[cur] + 1
                    q.enqueue(s)
    print()


#   3.3 I want to be tree

def __istree(g, v, parents):
    count = 1
    for s in range(g.order):
        if g.adj[v][s]:
            if parents[s] is None:
                parents[s] = v
                x = __istree(g, s, parents)
                if x == -1:
                    return -1
                count += x
            elif parents[v] != s:
                return -1
    return count

def istree(g):
    parents = [None] * g.order
    parents[0] = -1
    return __istree(g, 0, parents) == g.order

#   3.5 Compilation, cooking,...

def halfdegrees(g):
    ihd = [0] * g.order
    for v in range(g.order):
        for s in g.adjlists(v):
            ihd[s] += 1
    return ihd

def is_topo2(g, vect):
    ihd = halfdegrees(g)
    for v in vect:
        if ihd[v] != 0:
            return False
        for s in g.adjlists[v]:
            ihd[s] -= 1
    return True
