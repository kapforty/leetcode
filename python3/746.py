class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        for val in cost:
            dp.append(min(val + dp[-2], val + dp[-1]))
        return min(dp[-1], dp[-2])
