class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5]

        if n <= 3:
            return dp[n-1]

        for _ in range(n-3):
            dp.append((2*dp[-1] + dp[-3]) % 1000000007)

        return dp[-1]
