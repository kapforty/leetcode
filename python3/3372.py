class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # build adjacency lists
        edgeMap1, edgeMap2 = defaultdict(list), defaultdict(list)
        for x, y in edges1:
            edgeMap1[x].append(y)
            edgeMap1[y].append(x)
        for x, y in edges2:
            edgeMap2[x].append(y)
            edgeMap2[y].append(x)

        # trivial case
        if k == 0:
            return [1] * len(edgeMap1)
        
        # dfs on both graphs
        counts1, counts2 = defaultdict(int), -inf
        for i in range(len(edgeMap1)):
            visited, frontier = {i}, [(i, 0)]
            while frontier:
                curr, numEdges = frontier.pop()
                for node in edgeMap1[curr]:
                    if node not in visited and numEdges < k:
                        visited.add(node)
                        frontier.append((node, numEdges + 1))
            counts1[i] = len(visited)
        for i in range(len(edgeMap2)):
            visited, frontier = {i}, [(i, 0)]
            while frontier:
                curr, numEdges = frontier.pop()
                for node in edgeMap2[curr]:
                    if node not in visited and numEdges < k - 1:
                        visited.add(node)
                        frontier.append((node, numEdges + 1))
            counts2 = max(counts2, len(visited))
        
        # build result
        res = []
        for i in range(len(edgeMap1)):
            res.append(counts1[i] + counts2)
        return res
