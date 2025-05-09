class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minM, minN = m, n
        for x, y in ops:
            minM, minN = min(minM, x), min(minN, y)
        return minM * minN
