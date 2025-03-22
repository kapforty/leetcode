class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        res, edgeMap, visited = 0, defaultdict(set), set()
        for x, y in edges:
            edgeMap[x].add(y)
            edgeMap[y].add(x)

        def dfs(node, curr):
            for neighbor in edgeMap[node]:
                if neighbor not in curr:
                    curr.add(neighbor)
                    curr |= dfs(neighbor, curr)
            return curr
        
        for i in range(n):
            if i in visited:
                continue
            temp = dfs(i, {i})
            visited |= temp
            numEdges = 0
            for node in temp:
                numEdges += len(edgeMap[node])
            numEdges //= 2
            if numEdges == len(temp) * (len(temp) - 1) / 2:
                res += 1
        return res
