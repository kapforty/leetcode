class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1,1,1,1,1]
        n -= 1 
        while n > 0:
            for i in range(3, -1, -1):
                dp[i] += dp[i+1]
            n -= 1
        return sum(dp)
