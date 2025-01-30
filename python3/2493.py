class Solution:
    def isBipartite(self, graph, n) -> bool:
        color = [-1] * (n + 1)
        for i in range(n + 1):
            if color[i] == -1:
                color[i] = 0
                frontier = deque([i])
                while frontier:
                    curr = frontier.popleft()
                    for nextNode in graph[curr]:
                        if color[nextNode] == -1:
                            color[nextNode] = 1 - color[curr]
                            frontier.append(nextNode)
                        elif color[nextNode] == color[curr]:
                            return False
        return True

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        if not self.isBipartite(adjList, n):
            return -1
        
        def getNodes(n):
            nodes, frontier = {n}, [n]
            while frontier:
                curr = frontier.pop()
                for node in adjList[curr]:
                    if node not in nodes:
                        nodes.add(node)
                        frontier.append(node)
            return nodes

        def bfs(n):
            visited, frontier, count = {n}, [n], 0
            while frontier:
                nextFrontier = []
                count += 1
                for node in frontier:
                    for nextNode in adjList[node]:
                        if nextNode in visited:
                            continue
                        visited.add(nextNode)
                        nextFrontier.append(nextNode)
                frontier = nextFrontier
            return count

        res, visited = 0, set()
        for i in range(1, n+1):
            if i in visited:
                continue
            nodes, maxGroups = getNodes(i), 0
            visited.update(nodes)
            for node in nodes:
                groups = bfs(node)
                if groups == -1:
                    return -1
                maxGroups = max(maxGroups, groups)
            res += maxGroups
        return res    
