class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneCount = window = nums.count(1)
        zeroCount = nums[:window].count(0)
        nums = nums + nums
        res = zeroCount
        for i in range(window, len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                oneCount += 1
            if nums[i - window] == 0:
                zeroCount -= 1
            else:
                oneCount -= 1
            res = min(res, zeroCount)
        return res
            
