class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # trivial cases
        if not s1 or not s2:
            return s1 == s3 or s2 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        # setup dp matrix & first row/col
        dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        for col in range(1, len(dp[0])):
            dp[0][col] = dp[0][col-1]
            if s3[dp[0][col-1]] == s1[col-1]:
                dp[0][col] += 1
        for row in range(1, len(dp)):
            dp[row][0] = dp[row-1][0]
            if s3[dp[row-1][0]] == s2[row-1]:
                dp[row][0] += 1
        
        # dp
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                if dp[row-1][col] == dp[row][col-1]:
                    if s3[dp[row][col]] == s1[col-1] or s3[dp[row][col]] == s2[row-1]:
                        dp[row][col] += 1
                elif dp[row][col-1] > dp[row-1][col]:
                    if s3[dp[row][col]] == s1[col-1]:
                        dp[row][col] += 1
                else:
                    if s3[dp[row][col]] == s2[row-1]:
                        dp[row][col] += 1
        
        return dp[-1][-1] == len(s3)


        # s3:  a a d b b c b c a c
        # idx: 0 1 2 3 4 5 6 7 8 9
        
        # --- dp matrix setup ---
        #          a a b c c 
        #        0 1 2 2 2 2
        #      d 0 1 3 4 4 4
        #      b 0 2 4 5 6 6
        #      b 0 2 5 5 7 8
        #      c 0 2 6 7 8 9
        #      a 1 2 6 7 9 10     
