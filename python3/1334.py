class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        edgeMap = defaultdict(list)
        for x, y, dist in edges:
            edgeMap[x].append([dist, y])
            edgeMap[y].append([dist, x])
        
        res, minNeighbors = n-1, float("inf")

        for i in range(n):
            frontier = [[0, i]]
            heapq.heapify(frontier)
            visited = set()
            while frontier:
                currDist, curr = heapq.heappop(frontier)
                if curr not in visited:
                    visited.add(curr)
                    for dist, dest in edgeMap[curr]:
                        if currDist + dist <= distanceThreshold:
                            heapq.heappush(frontier, [currDist + dist, dest])

            if len(visited) - 1 <= minNeighbors:
                res, minNeighbors = i, len(visited) - 1

        return res



