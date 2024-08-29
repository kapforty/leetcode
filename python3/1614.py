class Solution:
    def maxDepth(self, s: str) -> int:
        res = curr = 0
        for char in s:
            if char == "(":
                curr += 1
                res = max(res, curr)
            if char == ")":
                curr -= 1
        return res
