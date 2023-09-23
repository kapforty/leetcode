class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)//2
            prev = nums[mid-1] if mid != 0 else float("-inf")
            post = nums[mid+1] if mid != len(nums) - 1 else float("inf")

            if nums[mid] > prev and nums[mid] > post:
                return mid
            elif nums[mid] <= post:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
