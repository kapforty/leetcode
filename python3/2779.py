class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = r = 0
        while r < len(nums):
            if nums[l] + k >= nums[r] - k:
                r += 1
            else:
                l += 1
                r += 1
        return r - l
