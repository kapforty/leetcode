class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # map edges, map in/out edge counts for each node
        edgeMap, nodeMap = defaultdict(deque), defaultdict(lambda: [0,0])
        for x, y in pairs:
            edgeMap[x].append(y)
            nodeMap[x][1] += 1
            nodeMap[y][0] += 1
        
        # find starting node
        startingNode = None
        for k, v in nodeMap.items():
            startingNode = k
            if v[1] > v[0]:
                break

        # calculate eulerian path
        tail = []
        path = [startingNode]
        edgeCount = len(pairs)
        while edgeCount > 0:
            if edgeMap[path[-1]]:
                curr = edgeMap[path[-1]].pop()
                nodeMap[path[-1]][1] -= 1
                nodeMap[curr][0] -= 1
                path.append(curr)
                edgeCount -= 1
            else:
                tail.append(path.pop())
                while len(path) > 1 and not edgeMap[path[-1]]:
                    nodeMap[path[-1]][0] += 1
                    nodeMap[path[-2]][1] += 1
                    edgeMap[path[-2]].append(path[-1])
                    path.pop()
                    edgeCount += 1
                temp = edgeMap[path[-1]].pop()
                edgeMap[path[-1]].appendleft(temp)
        path = path + tail[::-1]

        # build res
        res = []
        for i in range(len(path) - 1):
            res.append([path[i], path[i + 1]])
        return res
