class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # setup charMap
        charMap = defaultdict(int)
        for c in s:
            charMap[c] += 1

        # check if solution exists
        if charMap["a"] < k or charMap["b"] < k or charMap["c"] < k:
            return -1

        # two pointer
        res = len(s)
        l = 0
        for r in range(len(s)):
            charMap[s[r]] -= 1
            while charMap[s[r]] < k and l <= r:
                charMap[s[l]] += 1
                l += 1
            res = min(res, l + len(s) - r - 1)
        return res
