class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = high = diff = 0
        for num in nums:
            res = max(res, diff * num)
            diff = max(diff, high - num)
            high = max(high, num)
        return res
