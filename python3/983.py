class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        curr = 1
        for day in days:
            while curr < day:
                dp[curr] = dp[curr - 1]
                curr += 1
            oneDay = costs[0] + dp[curr - 1] if curr >= 1 else costs[0]
            sevenDay = costs[1] + dp[curr - 7] if curr >= 7 else costs[1]
            thirtyDay = costs[2] + dp[curr - 30] if curr >= 30 else costs[2]
            dp[curr] = min(oneDay, sevenDay, thirtyDay)
            curr += 1
        return dp[-1]
