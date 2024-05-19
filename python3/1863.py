class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def bt(curr, i):
            nonlocal res
            temp = curr ^ nums[i]
            res += temp
            for j in range(i+1, len(nums)):
                bt(temp, j)
        for i in range(len(nums)):
            bt(0, i)
        return res
