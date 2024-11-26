class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        candidates = set(range(n))
        for _, y in edges:
            if y in candidates:
                candidates.remove(y)
        return -1 if len(candidates) != 1 else candidates.pop()
