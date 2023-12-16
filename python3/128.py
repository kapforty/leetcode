class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums:
                continue
            length = 1
            while num + length in nums:
                length += 1
            res = max(res, length)
        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if n-1 in numSet:
                continue
            length = 1
            while n + length in numSet:
                length += 1
            longest = max(longest, length)

        return longest
