class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)
        dp = [[0 for _ in range(word1Len)] + [word2Len - i] for i in range(word2Len)]
        dp.append([word1Len - i for i in range(word1Len + 1)])
        
        for row in range(word2Len - 1, -1, -1):
            for col in range(word1Len - 1, -1, -1):  
                if word1[col] == word2[row]:
                    dp[row][col] = dp[row + 1][col + 1]
                else:
                    dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1])
        
        return dp[0][0]
