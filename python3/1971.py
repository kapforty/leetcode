class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # create adjacency list
        adjList = defaultdict(set)
        for n1, n2 in edges:
            adjList[n1].add(n2)
            adjList[n2].add(n1)

        # bfs
        visited = {source}
        frontier = deque([source])
        while frontier:
            curr = frontier.popleft()
            if curr == destination:
                return True
            for neighbor in adjList[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.append(neighbor)

        return False
