class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        curr = 0
        for num in nums:
            curr ^= num

        best = 2 ** maximumBit - 1
        res = []
        while nums:
            res.append(curr ^ best)
            curr ^= nums.pop()
        return res
