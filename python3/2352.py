class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(int), defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1
        for i in range(len(grid[0])):
            cols[tuple(row[i] for row in grid)] += 1
        
        res = 0
        for row in rows.keys():
            if row in cols:
                res += rows[row] * cols[row]

        return res
