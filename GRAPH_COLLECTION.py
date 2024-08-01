#GRAPH CREATION USING COLLECTIONS:
from collections import defaultdict
class Graph():
    def __init__(self):
        self.graph = defaultdict(dict)

    def addEdge(self, u, v,w):
        self.graph[u][v]=w
        self.graph[v][u]=w  # for undirected graph

g = Graph()
g.addEdge(0, 1,3)
g.addEdge(0, 2,4)
g.addEdge(1, 2,5)
g.addEdge(2, 0,6)
g.addEdge(2, 3,7)
g.addEdge(3, 3,8)

print(g.graph)


