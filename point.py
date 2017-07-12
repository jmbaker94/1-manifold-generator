

class Point:
    def __init__(self, data):
        self.x = data['x']
        self.y = data['y']
        self.z = data['z']


def distance(p1, p2, metric="euclidean"):
    if metric == "euclidean":
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2) ** (1/2)
    else:
        print("point-distance: invalid metric given.")
        return None

