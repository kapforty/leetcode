class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charMap = {}
        res = 0
        maxChar = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            maxChar = max(maxChar, charMap[s[r]])
            while r-l+1-maxChar > k:
                charMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
