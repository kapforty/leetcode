class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        res, dp = 0, [defaultdict(int) for _ in range(len(nums))]
        for r in range(1, len(nums)):
            for l in range(r):
                temp = dp[l][(nums[l]+nums[r])%k] + 1
                dp[r][(nums[l]+nums[r])%k] = max(dp[r][(nums[l]+nums[r])%k], temp)
                res = max(res, temp)
        return res + 1
