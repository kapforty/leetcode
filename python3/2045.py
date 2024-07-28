class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        edgeMap = defaultdict(list)
        for x, y in edges:
            edgeMap[x].append(y)
            edgeMap[y].append(x)

        visit = [0 for _ in range(n+1)]
        elapsed = 0
        frontier = {1}
        cycle = change * 2

        while frontier:
            remainder = elapsed % (cycle)
            if remainder >= change:
                elapsed += cycle - remainder
            elapsed += time
            nextFrontier = set()
            for node in frontier:
                visit[node] += 1
                for neighbor in edgeMap[node]:
                    if visit[neighbor] < 2:
                        nextFrontier.add(neighbor)
            if n in nextFrontier and visit[n]:
                    return elapsed
            frontier = nextFrontier
