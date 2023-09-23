class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(nums, count, valid):
            if count == k:
                if sum(nums) == n:
                    res.append(nums)
                return
            
            for i in range(valid, 10):
                backtrack(nums + [i], count + 1, i + 1)
                
        backtrack([], 0, 1)

        return res
