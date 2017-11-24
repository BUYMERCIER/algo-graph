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
    #for v in range(g.order):
        #for s in range(g.order if ):
            #pass
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
    src =  vertex we want to start with
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

def __bfs_mat(g, src, parents):
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

def breadth_first_full_traversal(g, src=0):
    parents = [None] * g.order
    parents[src] = -1
    __bfs(g, src, parents)
    for v in range(g.order):
        if parents[v] is None:
            parents[v] = -1
            __bfs(g, v, parents)
    return parents

def bfs_all_options(g, src=None, full=False):
    if src is None and not full:
        raise Exception("can't do that son")
    parents = [None] * g.order
    if src != None:
        parents[src] -= 1
        traversal(g, src, parents)
    if full:
        for v in range(g.order):
            if parents[v] is None:
                parents[v] = -1
                traversal(g, v, parents)
    return parents


################
#              #
#      DFS     #
#              #
################

# undirected graph
# def dfs(g, v, parents):
#   *pre-order job
#   * for all successors s of v
#       * if s has no parent:
#           * make v parent of s
#           * recursively continue on s
#       * otherwise
#           * if s is not the parent of v
#               * (v,s) is a backward edge
#   * post order job

def dfs(g, v, parents):
    print(v)
    # v = None
    for s in g.adjlists:
        if parents[s] is None:
            parents[s] = v
            dfs(g, s, parents)
        else:
            if parents[v] != s:
                print(v, '--', s, 'is a backward edge')





