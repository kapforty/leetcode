class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counts = defaultdict(int)
        for c in candidates:
            temp = str(bin(c))[2:][::-1]
            for i, val in enumerate(temp):
                if val == "1":
                    counts[i] += 1
        return max(counts.values())
