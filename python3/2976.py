class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # create map of edges
        edgeMap = defaultdict(list)
        for i in range(len(cost)):
            edgeMap[original[i]].append([cost[i], changed[i]])

        # precompute distances (dijkstra's)
        distMap = {}
        for char in source:
            if char in distMap:
                continue
            charMap = {}
            frontier = [[0, char]]
            heapq.heapify(frontier)
            while frontier:
                cost, curr = heapq.heappop(frontier)
                if curr in charMap:
                    continue
                charMap[curr] = cost
                for k, v in edgeMap[curr]:
                    if v in charMap:
                        continue
                    heapq.heappush(frontier, [cost + k, v])
            distMap[char] = charMap
        
        # calculate result
        res = 0
        for s, t in zip(source, target):
            if t not in distMap[s]:
                return -1
            res += distMap[s][t]
        return res
            
