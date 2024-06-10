class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        sortedHeights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                res += 1
        return res
