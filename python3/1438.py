class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        l = r = 0
        lower = upper = nums[0]
        vals = defaultdict(int)
        while r < len(nums):
            vals[nums[r]] += 1
            lower = min(lower, nums[r])
            upper = max(upper, nums[r])
            r += 1
            while upper - lower > limit:
                while lower in vals and upper in vals:
                    if l == r:
                        break
                    if vals[nums[l]] == 1:
                        del vals[nums[l]]
                    else:
                        vals[nums[l]] -= 1
                    l += 1
                lower = min(vals.keys())
                upper = max(vals.keys())
            res = max(res, r-l)
        return res
