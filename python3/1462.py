class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # create map of edges
        edges, prs = defaultdict(list), defaultdict(set)
        for x, y in prerequisites:
            edges[x].append(y)
        
        # dfs
        def dfs(curr):
            if len(edges[curr]) == 0:
                return
            while edges[curr]:
                node = edges[curr].pop()
                dfs(node)
                prs[curr].add(node)
                prs[curr].update(prs[node])
        for i in range(numCourses):
            dfs(i)
        
        # build result
        res = []
        for x, y in queries:
            res.append(True if y in prs[x] else False)
        return res
