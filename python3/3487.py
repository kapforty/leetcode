class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxVal = max(nums)
        if maxVal <= 0:
            return maxVal
        uniqueElements = set()
        for num in nums:
            if num > 0:
                uniqueElements.add(num)
        return sum(uniqueElements)
