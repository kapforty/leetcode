class Solution:
    def diameter(self, edgeList):
        # build adjacency matrix
        edgeMap, diameterMap = defaultdict(set), defaultdict(int)
        for x, y in edgeList:
            edgeMap[x].add(y)
            edgeMap[y].add(x)

        # first bfs
        n, frontier, visited = 0, [0], {0}
        while frontier:
            n, nextFrontier = frontier[0], []
            for node in frontier:
                for edge in edgeMap[node]:
                    if edge not in visited:
                        visited.add(edge)
                        nextFrontier.append(edge)
            frontier = nextFrontier
        
        # second bfs
        diameter, frontier, visited = -1, [n], {n}
        while frontier:
            diameter += 1
            nextFrontier = []
            for node in frontier:
                for edge in edgeMap[node]:
                    if edge not in visited:
                        visited.add(edge)
                        nextFrontier.append(edge)
            frontier = nextFrontier
        return diameter
                
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        diameter1, diameter2 = self.diameter(edges1), self.diameter(edges2)
        return max(diameter1, diameter2, ceil(diameter1/2) + ceil(diameter2/2) + 1)
