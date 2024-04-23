# PRUNE SOLUTION
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adjacency list
        adjList = defaultdict(set)
        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)

        # prune leaf nodes until two or less nodes are left
        toPrune = set()
        for node, neighbors in adjList.items():
            if len(neighbors) == 1:
                toPrune.add(node)
        while len(adjList) > 2:
            temp = set()
            for node in toPrune:
                neighbors = adjList[node]
                for neighbor in neighbors:
                    adjList[neighbor].remove(node)
                    if len(adjList[neighbor]) == 1:
                        temp.add(neighbor)
                del adjList[node]
            toPrune = temp

        return adjList.keys() if adjList else [0]

# BFS SOLUTION [TLE]
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adjacency list
        adjList = defaultdict(set)
        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)

        # bfs on each node, store result
        heights = defaultdict(int)
        for i in range(n):
            visited = {i}
            frontier = deque([[0, i]])
            while frontier:
                currHeight, curr = frontier.popleft()
                heights[i] = max(heights[i], currHeight)
                for neighbor in adjList[curr]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    frontier.append([currHeight + 1, neighbor])

        # calculate answer
        res = []
        for n, h in heights.items():
            if h == min(heights.values()):
                res.append(n)
        return res
