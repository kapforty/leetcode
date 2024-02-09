class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if matrix[row][col] == "0":
                    continue
                right = dp[row][col+1] if col + 1 < COLS else 0
                down = dp[row+1][col] if row + 1 < ROWS else 0
                diag = dp[row+1][col+1] if col + 1 < COLS and row + 1 < ROWS else 0
                dp[row][col] = 1 + min(right, down, diag)
                res = max(res, dp[row][col])
        
        return res**2
