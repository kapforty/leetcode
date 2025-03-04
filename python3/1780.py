class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 15
        for i in reversed(range(x)):
            temp = 3**i
            if temp <= n:
                n -= temp
        return n == 0
