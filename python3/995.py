class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = flips = 0
        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == 2:
                flips -= 1
            if (nums[i] + flips) % 2 == 0:
                if i + k > len(nums):
                    return -1
                nums[i] = 2
                res += 1
                flips += 1
        return res
