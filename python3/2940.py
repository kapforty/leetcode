class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # sort queries in descending order of y
        for i in range(len(queries)):
            x, y = queries[i]
            if x > y:
                queries[i] = [y, x]
        sortedQueries = sorted(queries, key=lambda x: x[1], reverse=True)
        
        # map query to index of building
        resMap = defaultdict(int)
        currIdx, stack = len(heights) - 1, []
        for x, y in sortedQueries:
            while currIdx >= y:
                while stack and heights[currIdx] >= stack[-1][0]:
                    stack.pop()
                stack.append((heights[currIdx], currIdx))
                currIdx -= 1
            if x == y or heights[x] < heights[y]:
                resMap[(x, y)] = y
            else:
                if not stack or stack[0][0] <= heights[x]:
                    resMap[(x, y)] = -1
                    continue
                l, r = 0, len(stack) - 1
                while l < r:
                    m = (l + r + 1) // 2
                    if stack[m][0] <= heights[x]:
                        r = m - 1
                    else:
                        l = m
                resMap[(x, y)] = stack[l][1]

        # extract values from resMap into res
        res = []
        for x, y in queries:
            res.append(resMap[(x, y)])
        return res
