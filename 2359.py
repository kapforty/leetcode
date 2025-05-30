class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # trivial case
        if node1 == node2:
            return node1

        # build adjacency lists
        edgeMap = defaultdict(list)
        for i, node in enumerate(edges):
            if node != -1:
                edgeMap[i].append(node)

        # bfs
        distanceMap1, distanceMap2 = {node1: 0}, {node2: 0}
        frontier1, frontier2 = deque([(node1, 0)]), deque([(node2, 0)])
        while frontier1:
            curr, dist = frontier1.popleft()
            for node in edgeMap[curr]:
                if node not in distanceMap1:
                    distanceMap1[node] = dist + 1
                    frontier1.append((node, dist + 1))
        while frontier2:
            curr, dist = frontier2.popleft()
            for node in edgeMap[curr]:
                if node not in distanceMap2:
                    distanceMap2[node] = dist + 1
                    frontier2.append((node, dist + 1))
        
        # calculate res
        res, minDist = -1, inf
        for i in range(len(edges)):
            if i in distanceMap1 and i in distanceMap2 and max(distanceMap1[i], distanceMap2[i]) < minDist:
                res, minDist = i, max(distanceMap1[i], distanceMap2[i])
        return res
