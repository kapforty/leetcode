class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq, visited = [(0, 0, 0)], {(0, 0)}
        while pq:
            time, r, c = heappop(pq)
            if r == len(moveTime) - 1 and c == len(moveTime[0]) - 1:
                return time
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if nr < 0 or nr >= len(moveTime) or nc < 0 or nc >= len(moveTime[0]) or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heappush(pq, (max(moveTime[nr][nc], time) + 1, nr, nc))
