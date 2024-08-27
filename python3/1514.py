class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # map node to edges/weight
        nodeMap = defaultdict(lambda: defaultdict(int))
        for i in range(len(edges)):
            nodeMap[edges[i][0]][edges[i][1]] = succProb[i] 
            nodeMap[edges[i][1]][edges[i][0]] = succProb[i]

        # modified dijkstra's algorithm
        frontier = {start_node}
        res = defaultdict(int)
        res[start_node] = 1
        while frontier:
            curr = frontier.pop()
            for next_node, prob in nodeMap[curr].items():
                temp = res[curr] * prob
                if temp > res[next_node]:
                    res[next_node] = temp
                    frontier.add(next_node)
        return res[end_node]