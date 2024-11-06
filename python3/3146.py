class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        idxMap = defaultdict(int)
        for i, c in enumerate(s):
            idxMap[c] = i
        for i, c in enumerate(t):
            res += abs(i - idxMap[c])
        return res
