class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, r = 0, len(nums) - 1
        for idx, num in enumerate(nums):
            while r >= 0 and nums[r] + num > target:
                r -= 1
            if r < idx:
                break
            res += 2**(r - idx)
            res %= 1000000007
        return res
