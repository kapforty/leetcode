class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = odd = 0
        for num in nums:
            if num % 2:
                odd += 1
            else:
                even += 1
        return [0] * even + [1] * odd
