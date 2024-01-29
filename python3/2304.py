class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # initialize dp array
        costs = [float("inf") for _ in range(len(grid[0]) * len(grid))]
        for i in grid[0]:
            costs[i] = 0
        
        # iterate through rows, calculating min cost of path to travel to next row
        for row in range(ROWS-1):
            for col in range(COLS):
                curr = grid[row][col]
                nextRow = grid[row+1]
                moveCosts = moveCost[curr]
                for idx in range(COLS):
                    costs[nextRow[idx]] = min(costs[nextRow[idx]], costs[curr] + moveCosts[idx] + curr)
        
        # calculate/return min value from last row in grid
        res = float("inf")
        for idx in grid[-1]:
            res = min(res, costs[idx] + idx)
        return res
