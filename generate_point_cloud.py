from point import Point
from graph import Graph, Vertex
import random


def generate_point_cloud(n=0):
    """
    :param n: size of the point cloud
    :return: a graph with no edges, g
    """
    if n < 3:
        print("generate_point_cloud: please give an n >= 3.")
        return None

    g = Graph()
    for i in range(n):
        g.vertices.append(Vertex({'point': Point({'x': random.random(), 'y': random.random(), 'z': random.random()}),
                                  'index': i}))

    return g
