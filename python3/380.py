class RandomizedSet:

    def __init__(self):
        self.dataMap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.dataMap:
            return False
        self.dataMap[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dataMap:
            return False
        idx1, idx2 = self.dataMap[val], len(self.data) - 1
        self.dataMap[self.data[-1]] = self.dataMap[val]
        self.data[idx1] = self.data[idx2]
        self.data.pop()
        self.dataMap.pop(val)
        return True

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data)-1)]
