class Solution:
    def fib(self, n: int) -> int:
        preceding = [0,1]
        if n < 2:
            return preceding[n]
        n -= 1
        while n > 0:
            temp = preceding[1]
            preceding[1] += preceding[0]
            preceding[0] = temp
            n -= 1
        return preceding[1]
