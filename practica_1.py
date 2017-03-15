class no_informed_list():
    def __init__(self):
        self.L = []
        self.start = 0

    def append(self, item):
        self.L.append(item)

    def extend(self, items):
        for item in items:
            self.L.append(item)

    def pop(self):
        less_cost = float('inf')
        index=-1
        for i, item in enumerate(self.L):
            if(item.path_cost<less_cost):
                less_cost=item.path_cost
                index = i
        if index == -1:
            return None
        else:
            return self.L.pop(index)

    def __len__(self):
        return len(self.L) - self.start


class informed_list():
    def __init__(self):
        self.L = []
        self.start = 0

    def append(self, item):
        self.L.append(item)

    def extend(self, items):
        for item in items:
            self.L.append(item)

    def pop(self):
        less_cost = float('inf')
        index=-1
        for i, item in enumerate(self.L):
            cost = item.path_cost+item.heuristic_cost
            if(cost<less_cost):
                less_cost=cost
                index = i
        if index == -1:
            return None
        else:
            return self.L.pop(index)

    def __len__(self):
        return len(self.L) - self.start