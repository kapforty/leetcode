class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l, nums = len(nums), set(nums)
        for i in range(2**l):
            curr = bin(i)[2:].zfill(l)
            if curr not in nums:
                return curr
