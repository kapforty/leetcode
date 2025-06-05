class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # create adjacency lists
        edgeMap1, edgeMap2 = defaultdict(list), defaultdict(list)
        for x, y in edges1:
            edgeMap1[x].append(y)
            edgeMap1[y].append(x)
        for x, y in edges2:
            edgeMap2[x].append(y)
            edgeMap2[y].append(x)
        
        # color the trees
        colorMap = {0: 0}
        colors = [0, 0]
        visited, frontier = {0}, [(0, 0)]
        while frontier:
            curr, color = frontier.pop()
            colors[color] += 1
            for node in edgeMap1[curr]:
                if node not in visited:
                    visited.add(node)
                    frontier.append((node, (color + 1) % 2))
                    colorMap[node] = (color + 1) % 2
        colors2 = [0, 0]
        visited, frontier = {0}, [(0, 0)]
        while frontier:
            curr, color = frontier.pop()
            colors2[color] += 1
            for node in edgeMap2[curr]:
                if node not in visited:
                    visited.add(node)
                    frontier.append((node, (color + 1) % 2))

        # build result
        res = []
        for i in range(len(edgeMap1)):
            res.append(colors[colorMap[i]] + max(colors2))
        return res
