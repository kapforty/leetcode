class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # precompute prefix sum
        prefixSum, prefixCount = [], 0
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                prefixCount += 1
            prefixSum.append(prefixCount)

        # calculate res
        res = []
        for s, e in queries:
            start = prefixSum[s - 1] if s - 1 >= 0 else 0
            end = prefixSum[e]
            res.append(end - start)
        return res
