class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            curr = a**2 + b**2
            if curr == c:
                return True
            elif curr < c:
                a += 1
            else:
                b -= 1
        return False
