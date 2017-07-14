from generate_point_cloud import *
from generate_1_manifold import *
from metrics import num_loops


def __main__():
    pc = generate_point_cloud(100)
    generate_1_manifold(pc)

    print(num_loops(pc))

__main__()
