class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # prefix/postfix sums
        for i in range(1, COLS):
            grid[1][i] += grid[1][i - 1]
        for i in range(COLS - 2, -1, -1):
            grid[0][i] += grid[0][i + 1]

        # calculate res
        res = inf
        for i in range(COLS):
            top = grid[0][i + 1] if i + 1 < COLS else 0
            bottom = grid[1][i - 1] if i - 1 >= 0 else 0
            res = min(res, max(top, bottom))
        return res
