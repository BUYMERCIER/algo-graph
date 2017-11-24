# from algopy.graph import *
from algopy.graphmat import *

def buildFromFile(path):
    with open(path) as file:
        directed = bool(int(file.readline()))
        order = int(file.readline())
        g = GraphMat(order, directed=directed)
        for line in file:
            src, dst = line.strip().split(' ')
            g.addedge(int(src), int(dst))
    return g

def degrees(g):
    vin, vout = [0] * g.order, []
    for l in g.adjlists:
        vout.append(len(l))
        for v in l:
            vin[v] += 1
    return vin, vout

def graph_half_degree(g):
    ind, outd = 0, 0
    

print("done")

# Exercise 1.5 (graphs)

def todot(g):
    out = ('di' * g.directed) + 'graph {\n'
    lnk = ' -> ' if g.directed else ' -- '
    for v in range(g.order):
        for s in g.acjlists[v]:
            if g.directed or v >= s:
                out += '\t' + str(v) + lnk + str(s) +'\n'
    return out + '}\n'

def todot_mat(g):
    out = ('di' * g.directed) + 'graph {\n'
    lnk = ' -> ' if g.directed else ' -- '
    for v in range(g.order):
        for s in range(g.order if ):
            pass
            # didn't finish


####################
#                  #
#    TRAVERSALS    #
#                  #
####################

# 2.1 BFS
# think about BFS -> think about QUEUES

from algopy.queues import *

def __bfs(g, src, parents):
    """
    g = the graph
    src = vertex we want to start with
    parents = a list of all the nodes and their parents
    """
    q = Queue()
    q.enqueue(src)
    while not q.isempty():
        cur = q.dequeue()
        for succ in g.adjlists[cur]:
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

################
#              #
#      DFS     #
#              #
################

def dfs(g, v):
    # mark v
    for s in g.adjlists:   
        pass









