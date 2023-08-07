class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1 : r]
        
        for i in range(len(s)):
            substringOne, substringTwo = helper(i, i), helper(i, i+1)
            if len(substringOne) > len(res):
                res = substringOne
            if len(substringTwo) > len(res):
                res = substringTwo

        return res
