class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        starts = [(0,0)] + [(0, i) for i in range(1, n)] + [(i, 0) for i in range(1, n)]
        while starts:
            r, c = starts.pop()
            tR, tC, values = r, c, []
            while tR < n and tC < n:
                values.append(grid[tR][tC])
                tR += 1
                tC += 1
            if c == 0:
                values.sort()
            else:
                values.sort(reverse=True)
            while r < n and c < n:
                grid[r][c] = values.pop()
                r += 1
                c += 1
        return grid
