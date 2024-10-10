class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxVals = [[nums[-1], len(nums) - 1]]
        for i, val in reversed(list(enumerate(nums[:-1]))):
            if val > maxVals[-1][0]:
                maxVals.append([val, i])  

        res = 0
        for i, num in enumerate(nums):
            curr = idx = None
            while maxVals and num <= maxVals[-1][0]:
                curr, idx = maxVals.pop()
            if curr == None:
                continue
            res = max(res, idx - i)
        return res
