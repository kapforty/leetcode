class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counts, MOD = deque([0]*26), 10**9+7
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for _ in range(t):
            counts[0] += counts[-1]
            counts.appendleft(counts[-1])
            counts.pop()
        return sum(counts) % MOD
