class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # dfs
        hashMap = {}
        def dfs(curr):
            if len(graph[curr]) == 0:
                hashMap[curr] = True
                return
            hashMap[curr] = False
            for edge in graph[curr]:
                if edge in hashMap:
                    continue
                dfs(edge)
            safe = True
            for edge in graph[curr]:
                if not safe:
                    break
                if hashMap[edge] == False:
                    safe = False
            hashMap[curr] = safe

        # run dfs on each node
        for node in range(len(graph)):
            if node not in hashMap:
                dfs(node)
        
        # build result
        res = []
        for k, v in hashMap.items():
            if v:
                res.append(k)
        return sorted(res)
