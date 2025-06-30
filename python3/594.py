class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res = r = 0
        for l, num in enumerate(nums):
            while r < len(nums) and nums[r] - num <= 1:
                r += 1
            if nums[r-1] - nums[l] == 1:
                res = max(res, r - l)
            if r == len(nums):
                break
        return res
