class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1Len, text2Len = len(text1) + 1, len(text2) + 1
        dp = [[0 for _ in range(text1Len)] for _ in range(text2Len)]
         
        for row in range(1, text2Len):
            for col in range(1, text1Len):
                if text2[row-1] == text1[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] += max(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]
