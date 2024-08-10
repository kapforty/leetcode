class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # CASE 1: REMOVE 0 ISLANDS
        # count number of islands
        numIslands, visited = 0, set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visited or grid[r][c] != 1:
                    continue
                numIslands += 1
                visited.add((r, c))
                frontier = [(r, c)]
                while frontier:
                    currX, currY = frontier.pop()
                    for x, y in directions:
                        tempR, tempC = currX + x, currY + y
                        if (tempR, tempC) in visited or tempR < 0 or tempR >= len(grid) or tempC < 0 or tempC >= len(grid[0]) or grid[tempR][tempC] != 1:
                            continue
                        visited.add((tempR, tempC))
                        frontier.append((tempR, tempC))
        if numIslands != 1:
            return 0

        # CASE 2: REMOVE 1 ISLAND
        # count number of islands when one is removed
        land = list(visited)
        for (row, col) in land:
            grid[row][col] = 0
            numIslands, visited = 0, set()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if (r, c) in visited or grid[r][c] != 1:
                        continue
                    numIslands += 1
                    visited.add((r, c))
                    frontier = [(r, c)]
                    while frontier:
                        currX, currY = frontier.pop()
                        for x, y in directions:
                            tempR, tempC = currX + x, currY + y
                            if (tempR, tempC) in visited or tempR < 0 or tempR >= len(grid) or tempC < 0 or tempC >= len(grid[0]) or grid[tempR][tempC] != 1:
                                continue
                            visited.add((tempR, tempC))
                            frontier.append((tempR, tempC))
            if numIslands != 1:
                return 1
            grid[row][col] = 1

        # CASE 3: REMOVE 2 ISLANDS
        return 2



