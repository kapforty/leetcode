class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(arr, nums):
            if not nums:
                res.append(arr)
                return
            for i in range(len(nums)):
                backtrack(arr + [nums[i]], nums[:i] + nums[i+1:])
        
        backtrack([], nums)
        return res
