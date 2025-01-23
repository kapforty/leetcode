class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rowMap, colMap = defaultdict(list), defaultdict(list)
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowMap[r].append((r, c))
                    colMap[c].append((r, c))
                    res += 1
        for curr in rowMap.values():
            if len(curr) < 2 and len(colMap[curr[0][1]]) < 2:
                res -= 1
        return res
