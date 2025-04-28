class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = cur = i = 0
        for j in range(len(nums)):
            cur += nums[j]
            while cur * (j - i + 1) >= k:
                cur -= nums[i]
                i += 1
            res += j - i + 1
        return res
