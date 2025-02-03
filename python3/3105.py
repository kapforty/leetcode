class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res, inc, dec = 0, [], []
        for num in nums:
            # process increasing subarray
            if not inc or num > inc[-1]:
                inc.append(num)
            else:
                res = max(res, len(inc))
                inc = [num]
            # process decreasing subarray
            if not dec or num < dec[-1]:
                dec.append(num)
            else:
                res = max(res, len(dec))
                dec = [num]
        return max(res, len(inc), len(dec))
