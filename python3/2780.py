class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        target = mode(nums)
        lCount, rCount = 0, nums.count(target)
        for i in range(len(nums) - 1):
            if nums[i] == target:
                lCount += 1
                rCount -= 1
            if lCount/(i+1) > 0.5 and rCount/(len(nums)-(i+1)) > 0.5:
                return i
        return -1
