class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        subgrid = [(0,0), (0,-1), (0,-2), (-1,0), (-1,-1), (-1,-2), (-2,0), (-2,-1), (-2,-2)]
        r = c = 2
        if r >= ROWS or c >= COLS:
            return res
        while r < ROWS:
            while c < COLS:
                visited = set()
                valid = True
                for x, y in subgrid:
                    if grid[r+x][c+y] in visited or grid[r+x][c+y] < 1 or grid[r+x][c+y] > 9:
                        valid = False
                        break
                    visited.add(grid[r+x][c+y])
                if valid:
                    target = grid[r-2][c-2] + grid[r-2][c-1] + grid[r-2][c]
                    if (grid[r-1][c-2] + grid[r-1][c-1] + grid[r-1][c] == target and 
                    grid[r][c-2] + grid[r][c-1] + grid[r][c] == target and
                    grid[r-2][c-2] + grid[r-1][c-2] + grid[r][c-2] == target and
                    grid[r-2][c-1] + grid[r-1][c-1] + grid[r][c-1] == target and
                    grid[r-2][c] + grid[r-1][c] + grid[r][c] == target and
                    grid[r-2][c-2] + grid[r-1][c-1] + grid[r][c] == target and
                    grid[r][c-2] + grid[r-1][c-1] + grid[r-2][c] == target):
                        res += 1
                c += 1
            r += 1
            c = 2
        return res

