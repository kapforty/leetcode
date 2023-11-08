class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        currSum = 0
        res = float("inf")

        while r < len(nums):
            currSum += nums[r]
            r += 1
            while currSum >= target:
                res = min(res, r - l)
                currSum -= nums[l]
                l += 1
        
        return 0 if res == float("inf") else res
