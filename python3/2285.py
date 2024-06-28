class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        numEdges = defaultdict(int)
        for x, y in roads:
            numEdges[x] += 1
            numEdges[y] += 1
        cities = sorted(numEdges.values(), reverse=True)
        res = 0
        for city in cities:
            res += city * n
            n -= 1
        return res
