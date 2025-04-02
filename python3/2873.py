class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = low = high = 0
        for num in nums:
            res = max(res, (high - low) * num)
            low = min(low, num)
            high = max(high, num)
        return res
