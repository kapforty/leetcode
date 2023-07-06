class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        charMap = {}
        minLen = float("inf")
        res = ""

        for char in t:
            charMap[char] = charMap.get(char, 0) + 1

        for r in range(len(s)):
            if s[r] not in charMap:
                continue
            charMap[s[r]] = charMap.get(s[r], 0) - 1
            while s[l] not in charMap or charMap[s[l]] < 0:
                if s[l] in charMap:
                    charMap[s[l]] = charMap.get(s[l], 0) + 1
                l += 1
            if max(charMap.values()) <= 0 and r-l+1 < minLen:
                minLen = r-l+1
                res = s[l:r+1]
            
        return res
