class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # two pointer: function to count number of pairs with a difference <= target
        nums.sort()
        def helper(target):
            l = r = count = 0
            while r < len(nums):
                if nums[r] - nums[l] > target:
                    l += 1
                    continue
                count += r - l
                r += 1
            return count
        
        # binary search
        l, r = 0, nums[-1]
        while l < r:
            m = (l + r) // 2
            if helper(m) < k:
                l = m + 1
            else:
                r = m
        return l
