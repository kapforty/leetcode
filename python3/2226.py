class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(num):
            piles = 0
            for c in candies:
                piles += c // num
            return True if piles >= k else False
        l, r = 0, max(candies)
        while l < r:
            m = (l + r + 1) // 2
            if valid(m):
                l = m
            else:
                r = m - 1
        return l
