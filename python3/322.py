class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        
        for i in range(1, amount + 1):
            minCoins = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    minCoins = min(minCoins, 1 + dp[i-coin])
            dp[i] = minCoins

        return -1 if dp[-1] == float("inf") else dp[-1]
