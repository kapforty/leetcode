class Solution:
    def findScore(self, nums: List[int]) -> int:
        # create heap
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))
        
        # process heap
        marked, score = set(), 0
        while len(marked) < len(nums):
            num, idx = heapq.heappop(heap)
            if idx in marked:
                continue
            if idx > 0:
                marked.add(idx - 1)
            marked.add(idx)
            if idx < len(nums) - 1:
                marked.add(idx + 1)
            score += num
        return score
