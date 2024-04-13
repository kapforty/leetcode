class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        heights = [0 for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            res = max(res, self.largestRectangle(heights))
        return res

    def largestRectangle(self, heights):
        maxRectangle = 0
        stack = []
        for i, h in enumerate(heights):
            idx = i
            while stack and h < stack[-1][0]:  
                temp = stack.pop()
                maxRectangle = max(maxRectangle, (i - temp[1]) * temp[0])
                idx = temp[1]
            stack.append([h, idx])
        for tempHeight, tempIdx in stack:
            maxRectangle = max(maxRectangle, (len(heights) - tempIdx) * tempHeight)
        return maxRectangle
