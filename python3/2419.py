class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = count = target = 0
        for num in nums:
            target = max(target, num)
        for num in nums:
            if num == target:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res
