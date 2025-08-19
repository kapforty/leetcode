class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = l = r = 0
        while l < len(nums):
            while l < len(nums) and nums[l] != 0:
                l += 1
            r = max(l, r)
            while r < len(nums) and nums[r] == 0:
                r += 1
                res += r - l
            l += 1
        return res
