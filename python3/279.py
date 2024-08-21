class Solution:
    def numSquares(self, n: int) -> int:
        # generate perfect squares
        perfectSquares = []
        i = 1
        while i ** 2 <= n:
            perfectSquares.append(i ** 2)
            i += 1
        
        # dp
        dp = [inf for _ in range(n + 1)]
        dp[0] = 0
        while perfectSquares:
            curr = perfectSquares.pop()
            for i in range(len(dp)):
                if i - curr < 0 or dp[i-curr] == inf:
                    continue
                dp[i] = min(dp[i], dp[i-curr] + 1)
        return dp[-1]
