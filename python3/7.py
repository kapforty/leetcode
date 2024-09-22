class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        res = int(str(abs(x))[::-1])
        if negative: res = 0 - res
        return res if (res > -2**31 and res <= 2**31-1) else 0
