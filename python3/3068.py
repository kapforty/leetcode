class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count = 0
        minSwap = float("inf")
        for i in range(len(nums)):
            temp = nums[i] ^ k
            minSwap = min(minSwap, abs(temp - nums[i]))
            if temp > nums[i]:
                count += 1
                nums[i] = temp
        res = sum(nums)
        if count % 2 != 0:
            res -= minSwap
        return res
