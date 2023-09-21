class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []

        ratios = defaultdict(list)
        for i in range(len(values)):
            equation = equations[i]
            ratios[equation[0]].append((equation[1], values[i]))
            ratios[equation[1]].append((equation[0], 1/values[i]))

        def evaluate(curr, target):
            if curr in ratios and target in ratios:
                frontier, visited = [(curr, 1)], set()
                while frontier:
                    node = frontier.pop()
                    visited.add(node[0])
                    if node[0] == target:
                        return node[1]
                    for x, y in ratios[node[0]]:
                        if x not in visited:
                            frontier.append((x, node[1] * y))
            return -1.0

        for query in queries:
            res.append(evaluate(query[0], query[1]))

        return res
