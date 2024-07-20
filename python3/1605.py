class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS, COLS = len(rowSum), len(colSum)
        res = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for i in range(len(rowSum)):
            curr = rowSum[i]
            j = 0
            while curr > 0:
                if curr >= colSum[j]:
                    res[i][j] += colSum[j]
                    curr -= colSum[j]
                    colSum[j] = 0
                    j += 1
                else:
                    res[i][j] += curr
                    colSum[j] -= curr
                    curr = 0
        return res
