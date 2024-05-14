class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # handle trivial cases
        if grid[0][0] or grid[-1][-1]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # convert zeroes to inf, ones to zero, add thieves to frontier/visited
        frontier = []
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    grid[r][c] = float("inf")
                else:
                    grid[r][c] = 0
                    heapq.heappush(frontier, (0, r, c))
                    visited.add((r,c))
        
        # calculate distance from thief cells
        while frontier:
            currVal, r, c = heapq.heappop(frontier)
            for x, y in directions:
                if (r + x, c + y) in visited or r + x < 0 or r + x >= ROWS or c + y < 0 or c + y >= COLS:
                    continue
                visited.add((r + x, c + y))
                heapq.heappush(frontier, (currVal + 1, r + x, c + y))
                grid[r + x][c + y] = currVal + 1

        # find max path
        frontier = []
        heapq.heappush(frontier, (grid[0][0], 0, 0))
        visited = {(0,0)}
        while frontier:
            currVal, r, c = heapq.heappop(frontier)
            currVal = -currVal
            if r == ROWS - 1 and c == COLS - 1:
                return currVal
            for x, y in directions:
                if (r + x, c + y) in visited or r + x < 0 or r + x >= ROWS or c + y < 0 or c + y >= COLS:
                    continue
                visited.add((r + x, c + y))
                grid[r + x][c + y] = min(grid[r][c], grid[r + x][c + y])
                heapq.heappush(frontier, (-grid[r + x][c + y], r + x, c + y))
