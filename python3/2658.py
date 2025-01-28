class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        def bfs(r, c):
            visited.add((r, c))
            frontier, fish = [(r, c)], grid[r][c]
            while frontier:
                r, c = frontier.pop()
                for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != 0 and (nr, nc) not in visited:
                        frontier.append((nr, nc))
                        visited.add((nr, nc))
                        fish += grid[nr][nc]
            return fish
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] != 0:
                    res = max(res, bfs(r, c))
        return res
