class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDist = nums[0]
        for i in range(len(nums) - 1):
            maxDist = max(maxDist, nums[i])
            if maxDist == 0:
                return False
            maxDist -= 1
        return True
