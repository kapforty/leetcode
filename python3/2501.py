class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums, res = set(nums), 0
        for num in nums:
            if num ** 0.5 in nums:
                continue
            length = 1
            while num ** 2 in nums:
                num **= 2
                length += 1
            res = max(res, length)
        return res if res >= 2 else -1
