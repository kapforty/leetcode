class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        res = []
        for i in range(len(weights) - 1):
            res.append(weights[i] + weights[i+1])
        res.sort()
        return sum(res[-k+1:]) - sum(res[:k-1])
