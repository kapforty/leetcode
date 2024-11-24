class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res, count, absMin = 0, 0, inf
        for row in matrix:
            for val in row:
                if val < 0:
                    count += 1
                absMin = min(absMin, abs(val))
                res += abs(val)
        return res if count % 2 == 0 else res - (absMin * 2)
