class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return sorted(nums) == [i+1 for i in range(len(nums) - 1)] + [len(nums) - 1]
