class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = maxV = 0
        for i, v in enumerate(arr):
            maxV = max(maxV, v)
            if i == maxV:
                res += 1
        return res
