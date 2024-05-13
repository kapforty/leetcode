class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # flip rows
        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = 0 if grid[r][c] == 1 else 1

        # flip cols
        for c in range(COLS):
            zeroCount = oneCount = 0
            for r in range(ROWS):
                if grid[r][c] == 0:
                    zeroCount += 1
                else:
                    oneCount += 1
            if zeroCount > oneCount:
                for r2 in range(ROWS):
                    grid[r2][c] = 0 if grid[r2][c] == 1 else 1

        # calculate answer
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += grid[r][c] * 2 ** (COLS-c-1)
        return res
