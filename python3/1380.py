class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in matrix:
            rowMin, idx1 = float("inf"), None
            for i in range(COLS):
                if row[i] < rowMin:
                    rowMin, idx1 = row[i], i
            colMax = rowMin
            for i in range(ROWS):
                if matrix[i][idx1] > colMax:
                    colMax = matrix[i][idx1]
                    break
            if rowMin == colMax:
                res.append(rowMin)
        return res
