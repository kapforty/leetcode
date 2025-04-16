class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res, numPairs, countMap = 0, 0, defaultdict(int)
        l = r = 0
        while r < len(nums):
            while r < len(nums) and numPairs < k:
                numPairs += countMap[nums[r]]
                countMap[nums[r]] += 1
                r += 1
            while numPairs >= k:
                res += len(nums) - r + 1
                countMap[nums[l]] -= 1
                numPairs -= countMap[nums[l]]
                l += 1
        return res
