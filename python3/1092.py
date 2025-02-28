class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ROWS, COLS = len(str2) + 1, len(str1) + 1
        dp = [None for _ in range(COLS)]
        dp[0] = ""
        for r in range(ROWS):
            newDP = []
            for c in range(COLS):
                temp, length = "", inf
                if r > 0:
                    up, upStr = len(dp[c]) + 1, dp[c] + str2[r-1]
                    if up < length: 
                        temp, length = upStr, up
                if c > 0:
                    left, leftStr = len(newDP[c-1]) + 1, newDP[c-1] + str1[c-1]
                    if left < length: 
                        temp, length = leftStr, left
                if r > 0 and c > 0 and str2[r-1] == str1[c-1]:
                    diag, diagStr = len(dp[c-1]) + 1, dp[c-1] + str1[c-1]
                    if diag < length: 
                        temp, length = diagStr, diag
                newDP.append(temp)
            dp = newDP
        return dp[-1]
