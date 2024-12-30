class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
        
        # calculate res
        res = 0
        for i in range(low, high+1):
            res += dp[i]
        return res % (10**9 + 7)
