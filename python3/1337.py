class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sort = []
        for i, line in enumerate(mat):
            sort.append((line.count(1), i))
        sort.sort()
        return [x[1] for x in sort[:k]]
