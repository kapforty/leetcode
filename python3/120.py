class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle = triangle[::-1]

        for row in range(len(triangle) - 1):
            for i in range(len(triangle[row]) - 1):
                triangle[row + 1][i] += min(triangle[row][i], triangle[row][i+1])

        return triangle[-1][-1]
