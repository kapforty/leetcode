class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        res = 0

        def dfs(y,x):
            for direction in directions:
                tempY, tempX = y + direction[0], x + direction[1]
                if tempY < 0 or tempY >= len(grid) or tempX < 0 or tempX >= len(grid[0]):
                    continue
                if (tempY, tempX) in visited or grid[tempY][tempX] == "0":
                    continue
                visited.add((tempY, tempX))
                dfs(tempY, tempX)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y,x) in visited:
                    continue
                if grid[y][x] == "1":
                    res += 1
                    visited.add((y, x))
                    dfs(y,x)

        return res
