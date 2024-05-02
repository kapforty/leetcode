class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        visited = set()
        for num in nums:
            if -num in visited:
                res = max(res, abs(num))
            visited.add(num)
        return res
