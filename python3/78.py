class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(curr, idx):
            res.append(curr)
            for i in range(idx, len(nums)):
                bt(curr + [nums[i]], i + 1)
        bt([], 0)
        return res
                
