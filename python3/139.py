class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            if dp[i] == False:
                continue
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    dp[i+len(word)] = True
        
        return dp[-1]
