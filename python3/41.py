class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first pass - execute swaps
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        # second pass - calculate answer
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return i + 2
