class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for num in nums:
            if parity != num % 2:
                return False
            parity = 1 - parity
        return True
