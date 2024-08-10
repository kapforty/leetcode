class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        res = 0

        # process grid and scale to 3x size
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == " ":
                    continue
                elif grid[r][c] == "/":
                    visited.add((r*3, c*3+2))
                    visited.add((r*3+1, c*3+1))
                    visited.add((r*3+2, c*3+0))
                else:
                    visited.add((r*3, c*3))
                    visited.add((r*3+1, c*3+1))
                    visited.add((r*3+2, c*3+2))

        # run dfs on all grid positions
        for r in range(len(grid)*3):
            for c in range(len(grid)*3):
                if (r,c) in visited:
                    continue
                res += 1
                visited.add((r,c))
                frontier = [(r,c)]
                while frontier:
                    currR, currC = frontier.pop()
                    for x, y in directions:
                        tempR, tempC = currR + x, currC + y
                        if (tempR, tempC) in visited or tempR < 0 or tempR >= len(grid) * 3 or tempC < 0 or tempC >= len(grid) * 3:
                            continue
                        visited.add((tempR, tempC))
                        frontier.append((tempR, tempC))
        
        return res
