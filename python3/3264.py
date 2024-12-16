class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        for _ in range(k):
            curr, idx = heapq.heappop(heap)
            heapq.heappush(heap, (curr * multiplier, idx))
        res = [0 for _ in range(len(nums))]
        for curr, idx in heap:
            res[idx] = curr
        return res
