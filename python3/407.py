class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        frontier = []
        res = maxHeight = 0

        # add border into frontier
        for i in range(COLS):
            heapq.heappush(frontier, (heightMap[0][i], 0, i))
            heightMap[0][i] = -1
            if heightMap[ROWS - 1][i] == -1: continue
            heapq.heappush(frontier, (heightMap[ROWS - 1][i], ROWS - 1, i))
            heightMap[ROWS - 1][i] = -1
        for i in range(1, ROWS - 1):
            heapq.heappush(frontier, (heightMap[i][0], i, 0))
            heightMap[i][0] = -1
            if heightMap[i][COLS - 1] == -1: continue
            heapq.heappush(frontier, (heightMap[i][COLS - 1], i, COLS - 1))
            heightMap[i][COLS - 1] = -1

        # bfs
        while frontier:
            h, r, c = heapq.heappop(frontier)
            maxHeight = max(maxHeight, h)
            res += maxHeight - h
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and heightMap[row][col] != -1:
                    heapq.heappush(frontier, (heightMap[row][col], row, col))
                    heightMap[row][col] = -1
        return res
