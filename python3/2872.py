class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # trivial case
        if n == 1:
            return 1

        # map nodes to values
        valMap = defaultdict(int)
        for i, v in enumerate(values):
            valMap[i] = v
        
        # map nodes to edges
        edgeMap = defaultdict(set)
        for x, y in edges:
            edgeMap[x].add(y)
            edgeMap[y].add(x)

        # find leaf nodes
        leafNodes = deque()
        for node, edges in edgeMap.items():
            if len(edges) < 2:
                leafNodes.append(node)
        
        # calculate result
        res = 0
        while edgeMap:
            curr = leafNodes.popleft()
            if valMap[curr] % k == 0:
                res += 1
            else:
                for n in edgeMap[curr]:
                    valMap[n] += valMap[curr]
            for n in edgeMap[curr]:
                edgeMap[n].remove(curr)
                if len(edgeMap[n]) < 2:
                    leafNodes.append(n)
            del edgeMap[curr]
        return res
                
            
