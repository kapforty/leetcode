class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                # left
                if c - 1 < 0:
                    res += 1
                elif grid[r][c-1] == 0:
                    res += 1
                # right
                if c + 1 == COLS:
                    res += 1
                elif grid[r][c+1] == 0:
                    res += 1
                # up
                if r - 1 < 0:
                    res += 1
                elif grid[r-1][c] == 0:
                    res += 1
                # down
                if r + 1 == ROWS:
                    res += 1
                elif grid[r+1][c] == 0:
                    res += 1
        return res
                
