class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if not len(str(num)) % 2:
                res += 1
        return res
