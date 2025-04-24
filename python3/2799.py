class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res, elements = 0, set(nums)
        for i in range(len(nums)):
            currElements = set()
            for j in range(i, len(nums)):
                currElements.add(nums[j])
                if elements == currElements:
                    res += 1
        return res
