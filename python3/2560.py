class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)

        while l < r:
            m = (l + r)//2
            size = 0
            i = 0
            while i < len(nums):
                if nums[i] <= m:
                    size += 1
                    i += 1
                i += 1
            if size >= k:
                r = m
            else:
                l = m + 1
        
        return l
