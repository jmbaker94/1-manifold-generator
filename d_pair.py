

class DPair:
    def __init__(self, pair, distance):
        self.pair = pair
        self.distance = distance

    def __lt__(self, other):
        if self.distance < other.distance:
            return True
        else:
            return False

