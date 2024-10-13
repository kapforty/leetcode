class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0 for _ in range(n + 1)]
        rides.sort()

        rIdx, i = 0, 1
        while i <= n:
            dp[i] = max(dp[i], dp[i-1])
            while rIdx < len(rides) and i == rides[rIdx][0]:
                start, end, tip = rides[rIdx]
                dp[end] = max(dp[end], end - start + tip + dp[start])
                rIdx += 1
            i += 1
        return max(dp)
