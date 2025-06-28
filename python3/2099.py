class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq, res = [], []
        for idx, num in enumerate(nums):
            heappush(pq, (-num, idx))
        for _ in range(k):
            num, idx = heappop(pq)
            res.append((idx, -num))
        res.sort()
        return [x[1] for x in res]
