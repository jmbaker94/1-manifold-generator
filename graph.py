from collections import defaultdict


class Vertex:
    def __init__(self, data):
        self.index = data['index']
        self.p = data['point']


class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_list = defaultdict(set)

