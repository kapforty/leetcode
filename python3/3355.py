class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        line = [0] * (len(nums) + 1)
        for x, y in queries:
            line[x] += 1
            line[y+1] -= 1
        numDec = 0
        for i, num in enumerate(nums):
            numDec += line[i]
            if num > numDec:
                return False
        return True
