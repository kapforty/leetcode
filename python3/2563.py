class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # trivial case
        if len(nums) < 2:
            return 0

        def findM(target, l, r):
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
                    
        res = 0
        nums.sort()
        l, r = -1, len(nums) - 1
        while l + 2 <= r:
            l += 1
            if nums[l] + nums[r] < lower:
                continue
            m = findM(lower - nums[l], l + 1, r)
            while r >= m and nums[l] + nums[r] > upper:
                r -= 1
            if l < m and m <= r:
                res += r - m + 1
        return res
