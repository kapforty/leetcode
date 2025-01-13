class Solution:
    def minimumLength(self, s: str) -> int:
        res, counter = 0, Counter(s)
        for k, v in counter.items():
            res += 2 if v % 2 == 0 else 1
        return res
