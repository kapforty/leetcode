class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        roads = defaultdict(list)
        for i in range(n - 1):
            roads[i].append(i+1)
        for x, y in queries:
            roads[x].append(y)
            distances = defaultdict(int)
            for i in range(1, n):
                distances[i] = inf
            frontier = [(0, 0)]
            while frontier:
                curr, cost = frontier.pop()
                for city in roads[curr]:
                    if distances[city] <= cost + 1:
                        continue
                    distances[city] = cost + 1
                    frontier.append((city, cost + 1))
            res.append(distances[n-1])
        return res
