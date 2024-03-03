class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # map trust relationships
        trustMap = defaultdict(list)
        trustMap2 = defaultdict(list)
        for x, y in trust:
            trustMap[x].append(y)
            trustMap2[y].append(x)

        # find judge
        res = -1
        for i in range(1, n+1):
            if i not in trustMap and len(trustMap2[i]) == n-1:
                if res > -1:
                    return -1
                else:
                    res = i
        return res
