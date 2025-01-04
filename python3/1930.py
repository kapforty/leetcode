class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = Counter(s)
        ends = []
        for k, v in counter.items():
            if v > 1:
                ends.append(k)
        visited = set()
        for v in ends:
            l, r = 0, len(s) - 1
            while s[l] != v:
                l += 1
            while s[r] != v:
                r -= 1
            for i in range(l + 1, r):
                visited.add((v, s[i], v))
        return len(visited)

