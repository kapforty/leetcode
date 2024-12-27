class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res, maxVal = values[0] + values[1] - 1, max(values[0] - 2, values[1] - 1)
        for val in values[2:]:
            res, maxVal = max(res, maxVal + val), max(maxVal - 1, val - 1)
        return res
