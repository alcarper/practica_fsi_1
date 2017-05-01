class no_informed_list:
    def __init__(self):
        self.L = []
        self.start = 0
        self.max_number = 0

    def append(self, item):
        self.L.append(item)
        self.max_number += 1


    def extend(self, items):
        for item in items:
            self.max_number += 1
            self.L.append(item)

    def pop(self):
        lesser_cost = float('inf')
        index = -1
        for i, item in enumerate(self.L):
            if item.path_cost < lesser_cost:
                lesser_cost = item.path_cost
                index = i
        if index == -1:
            return None
        else:
            return self.L.pop(index)

    def __len__(self):
        return len(self.L) - self.start


class informed_list:
    def __init__(self):
        self.L = []
        self.start = 0
        self.max_number = 0

    def append(self, item):
        self.L.append(item)
        self.max_number += 1

    def extend(self, items):
        for item in items:
            self.max_number += 1
            self.L.append(item)

    def pop(self):
        lesser_cost = float('inf')
        index = -1
        for i, item in enumerate(self.L):
            cost = item.path_cost+item.heuristic_cost
            if cost < lesser_cost:
                lesser_cost = cost
                index = i
        if index == -1:
            return None
        else:
            return self.L.pop(index)

    def __len__(self):
        return len(self.L) - self.start