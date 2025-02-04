class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, stack = 0, []
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                res = max(res, sum(stack))
                stack = [num]
        return max(res, sum(stack))
