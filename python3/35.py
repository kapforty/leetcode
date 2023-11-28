class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # trivial cases
        if target > nums[-1]: 
            return len(nums)
        if target < nums[0]: 
            return 0
            
        # binary search
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
