class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        curr = 1
        while r < len(nums):
            curr *= nums[r]
            r += 1
            while curr >= k and l < r:
                curr /= nums[l]
                l += 1
            res += r-l
        return res
