class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps)
        res = [[0] * arrLen for _ in range(steps + 1)]
        res[0][0] = 1
        for row in range(steps):
            for col in range(arrLen):
                res[row+1][col] += res[row][col]
                if col > 0:
                    res[row+1][col-1] += res[row][col]
                if col < arrLen-1:
                    res[row+1][col+1] += res[row][col]

        return res[-1][0] % (10 ** 9 + 7)
