class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counts = Counter(blocks[:k])
        res = counts['W']
        for i in range(k, len(blocks)):
            counts[blocks[i]] += 1
            counts[blocks[i-k]] -= 1
            res = min(res, counts['W'])
        return res
