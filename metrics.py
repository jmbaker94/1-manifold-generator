

def num_loops(mf=None):
    used_vertices = set()

    count = 0

    for v in mf.vertices:
        if v not in used_vertices:
            for e in list(walk_loop(mf, v)):
                used_vertices.add(e)
            count += 1

    return count


def walk_loop(mf=None, start=None):
    if mf is None or start is None:
        print("No manifold or start vertex given.")
        return None

    visited = {start}
    frontier = set(mf.adj_list[start])

    while len(frontier) != 0:
        v = frontier.pop()
        visited.add(v)
        for e in mf.adj_list[v]:
            if e not in visited:
                frontier.add(e)

    return visited
