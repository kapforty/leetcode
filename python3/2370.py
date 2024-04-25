class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = defaultdict(int)
        for char in s:
            dp[char] += 1
            for i in range(-k, k+1):
                temp = chr(ord(char) + i)
                if temp < "a" or temp > "z" or i == 0:
                    continue
                dp[char] = max(dp[char], dp[temp] + 1)
        return max(dp.values())
