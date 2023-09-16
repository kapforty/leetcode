class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = inf, inf
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True

        return False
