class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        unique = set()
        for k, v in counter.items():
            if v == 1:
                unique.add(k)
        if not unique:
            return -1
        for i in range(len(s)):
            if s[i] in unique:
                return i
