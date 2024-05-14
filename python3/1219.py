class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, pathSum):
            nonlocal res
            res = max(res, pathSum)
            for x, y in directions:
                if r + x < 0 or r + x >= ROWS or c + y < 0 or c + y >= COLS or grid[r + x][c + y] == 0:
                    continue
                temp = grid[r + x][c + y]
                grid[r + x][c + y] = 0
                dfs(r + x, c + y, pathSum + temp)
                grid[r + x][c + y] = temp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, 0)

        return res
