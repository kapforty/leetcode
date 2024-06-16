class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        nextVal = 1
        i = 0
        while nextVal <= n:
            if i < len(nums) and nums[i] <= nextVal:
                nextVal += nums[i]
                i += 1
            else:
                nextVal *= 2
                res += 1 
        return res
