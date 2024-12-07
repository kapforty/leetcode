class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        maxBags = len(nums) + maxOperations

        def valid(val):
            bags = 0
            for num in nums:
                bags += ceil(num/val)
            return bags <= maxBags

        while l < r:
            m = (l + r) // 2
            if valid(m):
                r = m
            else:
                l = m + 1
        return l
