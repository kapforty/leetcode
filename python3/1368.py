class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        h, visited = [], defaultdict(lambda: inf)
        heapq.heappush(h, (0, 0 ,0))
        visited[(0, 0)] = 0

        while h:
            cost, row, col = heapq.heappop(h)
            if row == ROWS - 1 and col == COLS - 1:
                return cost
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < ROWS and 0 <= c < COLS:
                    temp = cost
                    if ((dc == 1 and grid[row][col] != 1) or 
                        (dc == -1 and grid[row][col] != 2) or
                        (dr == 1 and grid[row][col] != 3) or
                        (dr == -1 and grid[row][col] != 4)):
                        temp += 1
                    if visited[(r, c)] > temp:
                        visited[(r, c)] = temp
                        heapq.heappush(h, (temp, r, c))
