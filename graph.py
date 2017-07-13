from collections import defaultdict


class Vertex:
    def __init__(self, data):
        self.index = data['index']
        self.p = data['point']


class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_list = defaultdict(set)

    def add_edge(self, u: Vertex, v: Vertex):
        if u not in self.vertices or v not in self.vertices:
            print("graph.add_edge: invalid vertices given.")
            return None

        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

