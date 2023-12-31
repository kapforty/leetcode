class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        indexes = defaultdict(int)
        for i, char in enumerate(s):
            if char not in indexes:
                indexes[char] = i
                continue
            res = max(res, i - indexes[char] - 1)
        return res
