class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # precompute island size
        curr, islandSize = 2, defaultdict(int)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 or grid[row][col] > 1:
                    continue
                frontier = [(row, col)]
                grid[row][col] = curr
                islandSize[curr] = 1
                while frontier:
                    r, c = frontier.pop()
                    for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                            grid[nr][nc] = curr
                            islandSize[curr] += 1
                            frontier.append((nr, nc))
                curr += 1
        
        # calculate size
        res = max(islandSize.values()) if islandSize else 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    continue
                islands = set()
                for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != 0:
                        islands.add(grid[nr][nc])
                currSize = 1
                for i in islands:
                    currSize += islandSize[i]
                res = max(res, currSize)
        return res
