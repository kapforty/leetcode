# --- O(N) RUNTIME COMPLEXITY ---
class Solution:
    def maxScore(self, s: str) -> int:
        res = zeros = 0
        ones = s.count("1")
        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            res = max(res, zeros + ones)
        return res

# --- O(N^2) RUNTIME COMPLEXITY ---
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            res = max(res, left.count("0") + right.count("1"))
        return res
