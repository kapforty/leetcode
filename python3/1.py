class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numMap:
                return [numMap[target - nums[i]], i]
            numMap[nums[i]] = i