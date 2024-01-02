class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adjList = defaultdict(list)
        visited = set()

        # build adjacency matrix
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])

        # define dfs algorithm
        def dfs(curr, path):
            if curr in visited:
                return True
            if curr in path:
                return False
            path.add(curr)
            for course in adjList[curr]:
                if not dfs(course, path):
                    return False
            path.remove(curr)
            visited.add(curr)
            res.append(curr)
            return True

        # topological sort
        for course in range(numCourses):
            if not dfs(course, set()):
                return []

        return res
