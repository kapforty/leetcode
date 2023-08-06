class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(houses):
            l, r = 0, 0
            for house in houses:
                temp = max(l + house, r)
                l = r
                r = temp
            return r
        
        return max(nums[0], dp(nums[:-1]), dp(nums[1:]))
