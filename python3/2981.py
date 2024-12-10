class Solution:
    def maximumLength(self, s: str) -> int:
        def valid(window):
            strMap = defaultdict(int)
            for i in range(len(s) - window + 1):
                if len(Counter(s[i:i+window])) == 1:
                    strMap[s[i:i+window]] += 1
                    if strMap[s[i:i+window]] >= 3:
                        return True
            return False

        l, r = 1, len(s) - 2
        if not valid(l):
            return -1
        while l < r:
            m = (l + r + 1) // 2
            if valid(m):
                l = m
            else:
                r = m - 1
        return l
