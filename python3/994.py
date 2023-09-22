class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        frontier = []
        oranges, rotten = 0, 0
        res = -1

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    frontier.append((r,c))
                    rotten += 1
                if grid[r][c] > 0:
                    oranges += 1

        if not oranges:
            return 0

        while frontier:
            res += 1
            for _ in range(len(frontier)):
                r, c = frontier.pop(0)
                for u, v in directions:
                    if r + u < 0 or c + v < 0 or r + u >= ROWS or c + v >= COLS:
                        continue
                    if grid[r + u][c + v] == 1:
                        frontier.append((r + u, c + v))
                        grid[r + u][c + v] = 2
                        rotten += 1

        return res if rotten == oranges else -1
