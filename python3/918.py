class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSubarray = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            total += num
            maxSubarray = max(total, maxSubarray)
        
        minSubarray = nums[0]
        total = 0
        for num in nums:
            if total > 0:
                total = 0
            total += num
            minSubarray = min(total, minSubarray)

        if maxSubarray < 0:
            return max(nums)
        return max(maxSubarray, sum(nums) - minSubarray)
