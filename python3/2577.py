class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # check if path exists
        if ROWS > 1 and COLS > 1 and grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        if ROWS > 1 and COLS == 1 and grid[1][0] > 1:
            return -1
        if ROWS == 1 and COLS > 1 and grid[0][1] > 1:
            return -1

        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        visited = {(0,0)}
        while heap:
            time, x, y = heapq.heappop(heap)
            if x == ROWS - 1 and y == COLS - 1:
                return time
            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS or (nx, ny) in visited:
                    continue
                tempTime = time + 1
                if grid[nx][ny] > tempTime:
                    tempTime = grid[nx][ny] + ((grid[nx][ny] - tempTime) % 2)
                visited.add((nx, ny))
                heapq.heappush(heap, (tempTime, nx, ny))
        return -1
