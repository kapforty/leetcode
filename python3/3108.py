class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        rank, parent = [0] * n, list(range(n))
        
        # implement union-find
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            pX, pY = find(x), find(y)
            if pX == pY:
                return
            if rank[pX] > rank[pY]:
                parent[pY] = pX
            elif rank[pX] < rank[pY]:
                parent[pX] = pY
            else:
                parent[pY] = pX
                rank[pX] += 1
        
        # run union-find on each edge
        for u, v, w in edges:
            union(u, v)

        # calculate costs of each disjoint set
        cost = defaultdict(int)
        for u, v, w in edges:
            p = find(u)
            if p not in cost:
                cost[p] = w
            else:
                cost[p] &= w

        # build result
        res = []
        for s, t in query:
            res.append(cost[find(s)] if find(s) == find(t) else -1)
        return res
