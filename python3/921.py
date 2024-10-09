class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = r = 0
        for p in s:
            if p == "(":
                l += 1
            elif l:
                l -= 1
            else:
                r += 1
        return l + r
