class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        visited = set(nums1)
        for num in nums2:
            if num in visited:
                return num
        return -1
