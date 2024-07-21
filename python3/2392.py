class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # convert row/col conditions to hashMaps
        rowMap, colMap = defaultdict(list), defaultdict(list)
        for x, y in rowConditions:
            rowMap[x].append(y)
        for x, y in colConditions:
            colMap[x].append(y)
        
        # create topological sort function
        def dfs(curr, visited, hashMap, path, rowOrCol):
            nonlocal cycleDetected
            if curr in path or cycleDetected:
                cycleDetected = True
                return
            if curr in visited:
                return
            visited.add(curr)
            path.add(curr)
            while hashMap[curr]:
                child = hashMap[curr].pop()
                dfs(child, visited, hashMap, path, rowOrCol)
            path.remove(curr)
            if rowOrCol == "r":
                rowTopo.append(curr)
            else:
                colTopo.append(curr)
        
        # run topological sort on row/col graphs
        rowTopo, colTopo = [], []
        rowVisited, colVisited = set(), set()
        cycleDetected = False
        for i in range(k):
            dfs(i+1, rowVisited, rowMap, set(), "r")
            dfs(i+1, colVisited, colMap, set(), "c")
        rowTopo, colTopo = rowTopo[::-1], colTopo[::-1]

        # check if cycle was detected
        if cycleDetected:
            return []

        # calculate positions of each value
        posRow, posCol = defaultdict(int), defaultdict(int)
        for i, val in enumerate(rowTopo):
            posRow[val] = i
        for i, val in enumerate(colTopo):
            posCol[val] = i

        # create res
        res = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1, k+1):
            res[posRow[i]][posCol[i]] = i
        return res
