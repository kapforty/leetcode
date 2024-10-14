class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        score = 0
        for _ in range(k):
            num = -heapq.heappop(maxHeap)
            score += num
            heapq.heappush(maxHeap, -ceil(num / 3))
        
        return score
