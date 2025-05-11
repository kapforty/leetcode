class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)), reverse=True)
        return nums[2] if len(nums) > 2 else nums[0]
