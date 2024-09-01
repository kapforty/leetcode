class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = []
        idx = 0
        for _ in range(m):
            res.append(original[idx:idx+n])
            idx += n
        return res