# O(n log(n))
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, nums[-1]
        while l <= r:
            target = (l + r) // 2
            i = 0
            while i < len(nums) and nums[i] < target:
                i += 1
            if len(nums) - i < target:
                r = target - 1
            elif len(nums) - i > target:
                l = target + 1    
            else:
                return target 
        return -1

# O(n log(n)) + O(mn)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for target in range(nums[-1] + 1):
            i = 0
            while i < len(nums) and nums[i] < target:
                i += 1
            if len(nums) - i == target:
                return target      
        return -1

