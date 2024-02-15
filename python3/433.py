class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        # helper function to check for valid mutation
        def validMutation(gene1, gene2):
            invalid = False
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    if invalid:
                        return False
                    invalid = True
            return True

        # bfs
        visited = set()
        frontier = deque([(startGene, 0)])
        while frontier:
            curr, res = frontier.popleft()
            visited.add(curr)
            if curr == endGene:
                return res
            for mutation in bank:
                if mutation in visited:
                    continue
                if validMutation(curr, mutation):
                    frontier.append((mutation, res + 1))
        return -1
