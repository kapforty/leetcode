class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([n for row in grid for n in row])
        median = nums[len(nums) // 2]
        res = 0
        for n in nums:
            if abs(n - nums[0]) % x != 0:
                return -1
            res += abs(n - median) // x
        return res
