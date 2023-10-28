class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1 for _ in range(5)] for _ in range(n)]

        for row in range(1, n):
            dp[row][0] = dp[row-1][1] + dp[row-1][2] + dp[row-1][4]
            dp[row][1] = dp[row-1][0] + dp[row-1][2]
            dp[row][2] = dp[row-1][1] + dp[row-1][3]
            dp[row][3] = dp[row-1][2]
            dp[row][4] = dp[row-1][2] + dp[row-1][3]

        return sum(dp[-1]) % (10**9 + 7)

# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         mapski = {"a":1, "e":1, "i":1, "o":1, "u":1}
#         rules = {"a": ["e"], "e": ["a", "i"], "i": ["a", "e", "o", "u"], "o": ["i", "u"], "u": ["a"]}

#         for i in range(n-1):
#             temp = defaultdict(int)
#             for k, v in mapski.items():
#                 for char in rules[k]:
#                     temp[char] += v
#             mapski = temp

#         return sum(mapski.values()) % (10**9+7)

            
