class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = list(zip(nums1, nums2))
        nums = sorted(nums, key=lambda p: p[1], reverse=True)
        
        heap = []
        currSum = 0
        res = 0

        for num1, num2 in nums:
            heapq.heappush(heap, num1)
            currSum += num1

            if len(heap) > k:
                currSum -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, currSum * num2)

        return res
