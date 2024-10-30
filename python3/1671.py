class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # calculate LIS
        LIS = [1 for _ in range(len(nums))]
        for i in range(1, len(nums) - 1):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        # calculate LDS
        LDS = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 2, 0, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        
        # calculate res
        res = 1000
        for i in range(len(nums)):
            if LIS[i] == 1 or LDS[i] == 1:
                continue
            res = min(res, len(nums) - LIS[i] - LDS[i] + 1)
        return res
