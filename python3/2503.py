class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        res = queries.copy()  
        queries = sorted(list(set(queries)), reverse=True)
        points, pointsMap = 0, defaultdict(int)
        frontier, visited = [(grid[0][0], 0, 0)], {(0, 0)}
        while queries:
            query = queries.pop()
            while frontier and frontier[0][0] < query:
                cell, r, c = heappop(frontier)
                points += 1
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited:
                        continue
                    heappush(frontier, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
            pointsMap[query] = points
        for i in range(len(res)):
            res[i] = pointsMap[res[i]]
        return res
