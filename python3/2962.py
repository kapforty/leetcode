class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = r = res = 0
        maxVal = max(nums)

        for i in range(len(nums)):
            if nums[i] == maxVal:
                k -= 1
            if k > 0:
                continue
            while k < 0:
                if nums[l] == maxVal:
                    k += 1
                l += 1
            while k == 0 and nums[l] != maxVal:
                l += 1
            res += l + 1
        
        return res