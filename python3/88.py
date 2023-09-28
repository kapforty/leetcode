class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m - 1
        idx2 = n - 1
        writeIdx = m + n - 1

        while writeIdx >= 0:
            num1 = float("-inf") if idx1 < 0 else nums1[idx1]
            num2 = float("-inf") if idx2 < 0 else nums2[idx2]
            if num1 >= num2:
                nums1[writeIdx] = num1
                idx1 -= 1
            else:
                nums1[writeIdx] = num2
                idx2 -= 1
            writeIdx -= 1

        return nums1

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[len(nums1)-len(nums2):] = nums2
#         nums1.sort()
#         return nums1
