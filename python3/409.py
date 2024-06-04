class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = odd = 0
        counter = Counter(s)
        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                odd = 1
        return res + 1 if odd else res
