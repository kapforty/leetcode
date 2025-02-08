class NumberContainers:

    def __init__(self):
        self.system = {}
        self.numToIdx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.system[index] = number
        heappush(self.numToIdx[number], index)

    def find(self, number: int) -> int:
        while self.numToIdx[number]:
            curr = self.numToIdx[number][0]
            if self.system[curr] == number:
                return curr
            heappop(self.numToIdx[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
