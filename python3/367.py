class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 0, num//2
        while l < r:
            m = (l + r) // 2
            if m**2 < num:
                l = m + 1
            else:
                r = m
        return l**2 == num
