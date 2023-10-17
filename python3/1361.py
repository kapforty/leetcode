class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find root
        rootCandidates = {i for i in range(n)}
        for i in range(n):
            rootCandidates.discard(leftChild[i])
            rootCandidates.discard(rightChild[i])
        if len(rootCandidates) != 1:
            return False
        
        # dfs from root
        visited = set()
        frontier = list(rootCandidates)
        while frontier:
            curr = frontier.pop()
            visited.add(curr)
            if leftChild[curr] != -1:
                if leftChild[curr] in visited:
                    return False
                frontier.append(leftChild[curr])
            if rightChild[curr] != -1:
                if rightChild[curr] in visited:
                    return False
                frontier.append(rightChild[curr])
        return len(visited) == n 
