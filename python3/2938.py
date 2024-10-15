class Solution:
    def minimumSteps(self, s: str) -> int:
        res = l = r = 0
        while r < len(s):
            if s[r] == "0":
                res += r - l
                l += 1
            r += 1
        return res
