class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(grid) - 2)] for _ in range(len(grid) - 2)]
        for r in range(1, len(grid)-1):
            for c in range(1, len(grid)-1):
                currMax = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        currMax = max(currMax, grid[r+x][c+y])
                res[r-1][c-1] = currMax
        return res
