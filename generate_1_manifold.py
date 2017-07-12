from d_pair import DPair
from point import *
import heapq


def assemble_heap(vertices):
    heap = []
    for v in vertices:
        for u in vertices:
            heapq.heappush(heap, DPair((v, u), distance(v.p, u.p)))


def generate_1_manifold(g=None):
    if g is None:
        print("generate_1_manifold: not point cloud given.")
        return None

    heap = assemble_heap(g.vertices)

    degrees = {}
    for v in g.vertices:
        degrees[v] = len(g.adj_list[v])

