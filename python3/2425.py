class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1) % 2 != 0:
            for num in nums2:
                res ^= num
        if len(nums2) % 2 != 0:
            for num in nums1:
                res ^= num
        return res
