class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = curr = big = small = 0
        for n in nums:
            curr += n
            res = max(res, abs(curr-big))
            res = max(res, abs(curr-small))
            big = max(big, curr)
            small = min(small, curr)
        return res
