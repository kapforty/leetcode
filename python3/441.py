class Solution:
    def arrangeCoins(self, n: int) -> int:
        rowSize = 1
        while n:
            if n >= rowSize:
                n -= rowSize
                rowSize += 1
            else:
                n = 0
        return rowSize - 1
