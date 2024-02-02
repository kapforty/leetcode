# --- RUNTIME O(N*M), SPACE O(N) ---
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = None
        for i in range(len(coins)):
            temp = [1] + [0 for _ in range(amount)]
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    temp[j] += temp[j-coins[i]]
                if dp:
                    temp[j] += dp[j]
            dp = temp
        return dp[-1]

# --- RUNTIME O(N*M), SPACE O(N*M) ---
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[1] + [0 for _ in range(amount)] for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
                if i > 0:
                    dp[i][j] += dp[i-1][j]
        return dp[-1][-1]
