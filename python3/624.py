class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        a, b = inf, -inf
        res = 0
        for arr in arrays:
            res = max(res, b - a + max(a - arr[0], arr[-1] - b))
            a = min(a, arr[0])
            b = max(b, arr[-1])
        return res
