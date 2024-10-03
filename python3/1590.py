class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        dp = {0: -1}
        curr = 0
        res = inf
        for i, num in enumerate(nums):
            curr = (curr + num) % p
            dp[curr] = i
            if (curr - need) % p in dp:
                res = min(res, i - dp[(curr - need) % p])
        return res if res < len(nums) else -1
