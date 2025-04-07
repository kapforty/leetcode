class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        if target != int(target):
            return False
        paths = {0}
        for num in nums:
            if target in paths:
                return True
            for path in list(paths):
                paths.add(path + num)
        return target in paths
