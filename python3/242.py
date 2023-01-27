class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMapS, charMapT = {}, {}
        for i in range(len(s)):
            charMapS[s[i]] = charMapS.get(s[i], 0) + 1
            charMapT[t[i]] = charMapT.get(t[i], 0) + 1
        return charMapS == charMapT