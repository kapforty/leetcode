class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = numZero = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZero += 1
            if numZero > 1:
                if nums[l] == 0:
                    numZero -= 1
                l += 1
        return r-l
