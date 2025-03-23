class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        edgeMap = defaultdict(set)
        for u, v, t in roads:
            edgeMap[u].add((v, t))
            edgeMap[v].add((u, t))

        counts, minTime, minHeap = {0: 1}, [inf] * n, [(0, 0)]
        while minHeap:
            time, curr = heappop(minHeap)
            if curr == n - 1: break
            for v, t in edgeMap[curr]:
                if v not in counts or (time + t < minTime[v]):
                    counts[v] = counts[curr]
                    heappush(minHeap, (time + t, v))
                    minTime[v] = time + t
                elif time + t == minTime[v]:
                    counts[v] += counts[curr]
        return counts[curr] % (10**9+7)
