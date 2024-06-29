class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(set)
        for x, y in edges:
            edgeMap[y].add(x)

        res = [[] for _ in range(n)]

        def dfs(node):
            if len(res[node]):
                return set(res[node])     
            ancestors = set()
            for ancestor in edgeMap[node]:
                ancestors.add(ancestor)
                ancestors.update(dfs(ancestor))   
            res[node] = sorted(ancestors)
            return ancestors
        
        for i in range(n):
            dfs(i)
        
        return res
