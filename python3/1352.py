class ProductOfNumbers:
    def __init__(self):
        self.stream = [1]
        self.lastIdx = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
            self.lastIdx = len(self.stream) - 1
        else:
            self.stream.append(num * self.stream[-1])

    def getProduct(self, k: int) -> int:
        size = len(self.stream)
        if size - k - 1 < self.lastIdx:
            return 0
        return self.stream[-1] // self.stream[size - k - 1]
