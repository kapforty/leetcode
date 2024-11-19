class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        window, windowSum = defaultdict(int), 0

        # setup initial window
        for num in nums[:k]:
            window[num] += 1
            windowSum += num
        if len(window) == k:
            res = max(res, windowSum)

        # sliding window
        for i in range(k, len(nums)):
            window[nums[i]] += 1
            if window[nums[i-k]] == 1:
                del window[nums[i-k]]
            else:
                window[nums[i-k]] -= 1
            windowSum += nums[i] - nums[i-k]
            if len(window) == k:
                res = max(res, windowSum)
        return res
