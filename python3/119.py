class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[0] * (rowIndex + 1) for _ in range(rowIndex + 1)]
        dp[0][0] = 1

        for idx, row in enumerate(dp):
            if idx == 0:
                continue
            for col in range(idx + 1):
                dp[idx][col] += dp[idx-1][col]
                if col > 0:
                    dp[idx][col] += dp[idx-1][col-1]
        
        return dp[-1]
