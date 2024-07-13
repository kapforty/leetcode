class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        curr = 1
        while curr < n:
            curr *= 2
        return curr == n
