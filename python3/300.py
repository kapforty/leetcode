class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            LIS = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS = max(LIS, dp[j])
            dp[i] = 1 + LIS
        
        return max(dp)
