class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        lenHeights = len(heights)

        for i in range(lenHeights):
            idx = i
            while stack and stack[-1][0] > heights[i]:
                tempHeight, tempIdx = stack.pop()
                idx = tempIdx
                res = max(res, (i - tempIdx) * tempHeight)
            stack.append([heights[i], idx])
        
        for tempHeight, tempIdx in stack:
            res = max(res, (lenHeights - tempIdx) * tempHeight)

        return res
