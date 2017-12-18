def bfs(g, src=0):
	parents = [None] * g.order
	parents[src] = -1
	_bfs(g, src, parents)
	for v in range(g.order):
		if parents[v] is None:
			parents[v] = -1
			_bfs(g, v, parents)
	return parents

def _bfs(g, src, parents):
	q = Queue()
	q.enqueue(src)
	while not q.isempty():
		cur = q.dequeue()
		for i in range(g.order):
			if g.adj[cur][i]:
				if parents[i] is None:
					parents[i] = cur
					q.enqueue(i)