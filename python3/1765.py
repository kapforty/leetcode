class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        res = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        frontier = []
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    res[r][c] = 0
                    heappush(frontier, (0, r, c))

        while frontier:
            h, r, c = heappop(frontier)
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or res[nr][nc] != -1:
                    continue
                res[nr][nc] = h+1
                heappush(frontier, (h+1, nr, nc))
        return res
