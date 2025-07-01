class Solution:
    def possibleStringCount(self, word: str) -> int:
        res, prev, curr = 1, None, 1
        for s in word:
            if s != prev:
                res += curr - 1
                prev, curr = s, 1
            else:
                curr += 1
        return res + curr - 1
