class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = curr = 0
        sumski = sum(nums)
        for num in nums[:-1]:
            sumski -= num
            curr += num
            if curr >= sumski:
                res += 1
        return res
