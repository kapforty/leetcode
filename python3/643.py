class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = currSum = sum(nums[:k])
        
        for i in range(k, len(nums), 1):
            currSum -= nums[i-k]
            currSum += nums[i]
            res = max(res, currSum)

        return res/k
