class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # calculate maximum possible bitwise OR
        target = 0
        for num in nums:
            target |= num

        # bt
        res = 0
        def bt(curr, nums):
            nonlocal res
            if curr == target:
                res += 1
            if not nums:
                return
            for i, num in enumerate(nums):
                bt(curr | num, nums[i+1:])
        bt(0, nums)
        return res
