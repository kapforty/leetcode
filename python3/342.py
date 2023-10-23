class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        curr = 1
        while curr < n:
            curr *= 4
        return curr == n
