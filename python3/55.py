class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        for i in range(len(nums) - 1):
            jumps = max(jumps, nums[i])
            if jumps == 0:
                return False
            jumps -= 1 
        return True
