class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        if n % 3 == 1:
            return 3**(n//3 - 1) * (n%3 + 3)
        if n % 3 == 2:
            return 3**(n//3) * 2
        else:
            return 3**(n//3)
