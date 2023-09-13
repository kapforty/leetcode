class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for prereq in prerequisites:
            courseMap[prereq[0]].append(prereq[1])
        
        visited = set()

        def dfs(curr):
            if curr in visited:
                return False
            if courseMap[curr] == []:
                return True
            visited.add(curr)
            for pre in courseMap[curr]:
                if not dfs(pre):
                    return False
            visited.remove(curr)
            courseMap[curr] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
