class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cost = defaultdict(lambda: inf)
        cost[(0,0)] = 0
        heap = [(0,0,0)]
        while heap:
            c, x, y = heapq.heappop(heap)
            if x == ROWS - 1 and y == COLS - 1:
                return c
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS:
                    continue
                temp = cost[(x,y)]
                if grid[nx][ny] == 1:
                    temp += 1
                if temp < cost[(nx,ny)]:
                    cost[(nx,ny)] = temp
                    heapq.heappush(heap, (temp, nx, ny))
        return cost[(ROWS-1, COLS-1)]
