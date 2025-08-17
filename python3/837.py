class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1
        res = 0
        dp = [0] * (n + 1)
        dp[0] = window = 1
        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]
            else:
                res += dp[i]
            if i - maxPts >= 0:
                window -= dp[i - maxPts]
        return res
