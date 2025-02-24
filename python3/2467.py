class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        edgeMap = defaultdict(list)
        for x, y in edges:
            edgeMap[x].append(y)
            edgeMap[y].append(x)
        
        # dfs to find bob's path to node 0
        bobPath = None
        def dfs(path, visited):
            nonlocal bobPath
            if bobPath:
                return
            if path[-1] == 0:
                bobPath = path.copy()
                return
            for node in edgeMap[path[-1]]:
                if node in visited:
                    continue
                path.append(node)
                visited.add(node)
                dfs(path, visited)
                path.pop()
                visited.remove(node)
        dfs([bob], {bob})

        # calculate time for alice to reach each node
        timeMap, frontier, currTime = {0: 0}, [0], 0
        while frontier:
            currTime += 1
            nextFrontier = []
            for node in frontier:
                for nextNode in edgeMap[node]:
                    if nextNode in timeMap:
                        continue
                    timeMap[nextNode] = currTime
                    nextFrontier.append(nextNode)
            frontier = nextFrontier
        
        # adjust node price/rewards
        for steps, node in enumerate(bobPath):
            if steps < timeMap[node]:
                amount[node] = 0
            elif steps == timeMap[node]:
                amount[node] //= 2

        # calculate optimal alice path
        res = -inf
        def dfs(node, visited, income):
            nonlocal res
            if node != 0 and len(edgeMap[node]) == 1:
                res = max(res, income)
                return
            for nextNode in edgeMap[node]:
                if nextNode in visited:
                    continue
                visited.add(nextNode)
                dfs(nextNode, visited, income + amount[nextNode])
                visited.remove(nextNode)
        dfs(0, {0}, amount[0])
        return res
