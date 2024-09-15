class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maskMap = {0: -1}
        res = bitmask = 0
        for i, c in enumerate(s):
            if c in vowels:
                bitmask ^= ord(c) - ord('a') + 1
            if bitmask in maskMap:
                res = max(res, i - maskMap[bitmask])
            else:
                maskMap[bitmask] = i
        return res
