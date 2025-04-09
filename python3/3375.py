class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        nums = set(nums)
        return len(nums) - 1 if k in nums else len(nums)
