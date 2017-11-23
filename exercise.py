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
        or s in range(g.order if ):
