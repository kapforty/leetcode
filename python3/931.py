class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        paths = matrix[0]

        for row in matrix[1:]:
            temp = [0] * len(paths)
            for col in range(len(paths)):
                l = m = r = float("inf")
                if col - 1 >= 0:
                    l = paths[col-1]
                m = paths[col]
                if col + 1 < len(matrix[0]):
                    r = paths[col+1]
                temp[col] = min(l, m, r) + row[col]
            paths = temp

        return min(paths)
