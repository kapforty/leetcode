class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for node, num in enumerate(isConnected[i]):
                if num:
                    dfs(node)

        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                dfs(i)

        return res
