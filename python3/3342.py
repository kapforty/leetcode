class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS, COLS = len(moveTime), len(moveTime[0])
        frontier, visited = [(0, 1, 0, 0)], {(0, 0)}
        while frontier:
            time, altTime, r, c = heappop(frontier)
            if r + 1 == ROWS and c + 1 == COLS:
                return time
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heappush(frontier, (
                    max(time, moveTime[nr][nc]) + altTime,
                    1 if altTime == 2 else 2,
                    nr,
                    nc
                ))
