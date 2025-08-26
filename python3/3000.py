class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = maxDiagonal = 0
        for l, w in dimensions:
            diagonal = l**2 + w**2
            if diagonal > maxDiagonal:
                res, maxDiagonal = l * w, diagonal
            elif diagonal == maxDiagonal:
                res, maxDiagonal = max(res, l * w), diagonal
        return res
