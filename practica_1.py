class no_informed_list:
    def __init__(self):
        self.L = []
        self.start = 0

    def append(self, item):
        self.L.append(item)

    def extend(self, items):
        for item in items:
            self.L.append(item)

    def pop(self):
        if len(self.L) == 0:
            return None
        lesser_cost = self.L[0].path_cost
        index = 0
        for i, item in enumerate(self.L):
            if item.path_cost < lesser_cost:
                lesser_cost = item.path_cost
                index = i
        return self.L.pop(index)

    def __len__(self):
        return len(self.L) - self.start


class informed_list:
    def __init__(self):
        self.L = []
        self.start = 0

    def append(self, item):
        self.L.append(item)

    def extend(self, items):
        for item in items:
            self.L.append(item)

    def pop(self):
        if len(self.L) == 0:
            return None
        lesser_cost = self.L[0].path_cost + self.L[0].heuristic_cost
        index = 0
        for i, item in enumerate(self.L):
            cost = item.path_cost + item.heuristic_cost
            if cost < lesser_cost:
                lesser_cost = cost
                index = i
        return self.L.pop(index)

    def __len__(self):
        return len(self.L) - self.start
