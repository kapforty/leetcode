class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {0: -1}
        currSum = 0
        for i, n in enumerate(nums):
            currSum += n
            remainder = currSum % k
            if remainder not in prefixSum:
                prefixSum[remainder] = i
            elif i - prefixSum[remainder] >= 2:
                    return True
        return False
