class Solution:
    def __init__(self):
        self.cache = {}

    def myPow(self, x: float, n: int) -> float: 
        if (x,n) in self.cache:
            return self.cache[(x,n)]
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1  
        if n == 1:
            return x
        res = self.myPow(x, n//2) * self.myPow(x, ceil(n/2))
        self.cache[(x,n)] = res
        return res