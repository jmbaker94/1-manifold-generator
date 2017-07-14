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

    def __contains__(self, edge):
        if edge[0] in self.adj_list[edge[1]] and edge[1] in self.adj_list[edge[0]]:
            return True
        else:
            return False

