class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, count1, sum2, count2 = sum(nums1), nums1.count(0), sum(nums2), nums2.count(0)
        sum1 += count1
        sum2 += count2
        if sum1 == sum2:
            return sum1
        if sum1 <= sum2 and count1:
            return sum2
        if sum1 >= sum2 and count2:
            return sum1
        return -1
