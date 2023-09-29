class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(row, col):
            count = 0
            frontier = [(row, col)]
            while frontier:
                r, c = frontier.pop()
                count += 1
                for x, y in directions:
                    if r + x < 0 or r + x >= ROWS or c + y < 0 or c + y >= COLS or grid[r + x][c + y] == 0:
                        continue
                    if (r + x, c + y) not in visited:
                        frontier.append((r + x, c + y))
                        visited.add((r + x, c + y))
            return count


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 or (row, col) in visited:
                    continue
                if grid[row][col] == 1:
                    visited.add((row, col))
                    res = max(res, dfs(row, col))
        return res
