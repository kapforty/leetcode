class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == col == 0:
                    continue
                up = grid[row-1][col] if row - 1 >= 0 else float("inf")
                left = grid[row][col-1] if col - 1 >= 0 else float("inf")
                grid[row][col] += min(up, left)
        return grid[-1][-1]
