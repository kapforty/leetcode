class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if (r, c) in visited or grid2[r][c] == 0:
                    continue
                visited.add((r, c))
                frontier = [(r, c)]
                valid = grid1[r][c] == 1
                while frontier:
                    curr = frontier.pop()
                    for x, y in directions:
                        currX, currY = x + curr[0], y + curr[1]
                        if (currX, currY) in visited or currX < 0 or currX >= len(grid2) or currY < 0 or currY >= len(grid2[0]) or grid2[currX][currY] == 0:
                            continue
                        visited.add((currX, currY))
                        frontier.append((currX, currY))
                        if grid1[currX][currY] == 0:
                            valid = False
                if valid:
                    res += 1
        return res
                        
