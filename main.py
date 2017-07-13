from generate_point_cloud import *
from generate_1_manifold import *


def __main__():
    pc = generate_point_cloud(10)
    generate_1_manifold(pc)


__main__()