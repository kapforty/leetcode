class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            if i + 2 < len(nums):
                nums[i] = (nums[i] + 1) % 2
                nums[i+1] = (nums[i+1] + 1) % 2
                nums[i+2] = (nums[i+2] + 1) % 2
                res += 1
            else:
                return -1
        return res
