from d_pair import DPair
from point import *
import heapq


def assemble_heap(vertex, graph):
    heap = []
    for v in graph.vertices:
        if v != vertex:
            heapq.heappush(heap, DPair((vertex, v), distance(vertex.p, v.p)))
    return heap


def generate_1_manifold(g=None):
    if g is None:
        print("generate_1_manifold: not point cloud given.")
        return None

    heap_list = {}
    degrees = {}
    for v in g.vertices:
        heap_list[v] = assemble_heap(v, g)
        degrees[v] = len(g.adj_list[v])

    # Ensure that each vertex gets 0 or 1 neighbor
    for v in g.vertices:
        if len(g.adj_list[v]) == 0:
            found = False
            i = 0
            while not found:
                i += 1
                if i == len(g.vertices):
                    found = True
                    g.add_edge(v, heapq.heappop(heap_list[v]).pair[1])

                q = heapq.heappop(heap_list[v]).pair[1]
                if len(g.adj_list[q]) == 0:
                    found = True
                    g.add_edge(v, q)
                heapq.heapify(heap_list[v])

    # Reset the heaps
    heap_list = {}
    for v in g.vertices:
        heap_list[v] = assemble_heap(v, g)

    # Ensure that each vertex gets up to 2 neighbors exactly
    for v in g.vertices:
        if len(g.ad_list[v]) < 2:
            found = False
            i = 0
            while not found:
                q = heapq.heappop(heap_list[v]).pair[1]
                if len(g.adj_list[q]) < 2:
                    found = True
                    g.add_edge(v, q)
                heapq.heapify(heap_list[v])

    # Sanity Check
    for v in g.vertices:
        if len(g.adj_list[v]) != 2:
            print("ERROR")
