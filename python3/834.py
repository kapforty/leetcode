class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adjacency list
        adjList = defaultdict(set)
        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)
        
        # dfs to calculate S.O.D. from node 0
        base = 0
        visited = {0}
        def dfs(node, count):
            nonlocal base
            base += count
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, count + 1)
        dfs(0, 0)

        # dfs to calculate number of nodes in subtrees
        subtreeCount = [0] * n
        visited = {0}
        def dfs2(node):
            count = 1
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    count += dfs2(neighbor)
            subtreeCount[node] = count
            return count
        dfs2(0)
        
        # dfs to calculate S.O.D. for remaining nodes
        res = [0] * n
        res[0] = base
        visited = {0}
        def dfs3(node, count):
            if node != 0:
                res[node] = count + n - 2 * subtreeCount[node]
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs3(neighbor, res[node])
        dfs3(0, base)

        return res

