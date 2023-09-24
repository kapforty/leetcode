class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(query_row + 1)]
        dp[0][0] = poured
        for row in range(query_row):
            for col in range(len(dp[row])):
                if dp[row][col] > 1:
                    split = (dp[row][col] - 1)/2
                    dp[row+1][col] += split
                    dp[row+1][col+1] += split

        return min(1, dp[query_row][query_glass])
