class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dp = [0 for _ in range(ROWS)]
        for c in range(COLS - 1):
            temp = [-1 for _ in range(ROWS)]
            for r in range(ROWS):
                if dp[r] == -1:
                    continue
                top = -1 if r-1 < 0 else grid[r-1][c+1]
                mid = grid[r][c+1]
                bot = -1 if r+1 >= ROWS else grid[r+1][c+1]
                if top > grid[r][c]:
                    temp[r-1] = dp[r] + 1
                    res = max(res, temp[r-1])
                if mid > grid[r][c]:
                    temp[r] = dp[r] + 1
                    res = max(res, temp[r])
                if bot > grid[r][c]:
                    temp[r+1] = dp[r] + 1
                    res = max(res, temp[r+1])
            dp = temp
        return res
