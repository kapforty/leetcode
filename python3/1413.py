class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mini = curr = 0
        for num in nums:
            curr += num
            mini = min(mini, curr)
        return abs(mini) + 1 if mini <= 0 else 1
