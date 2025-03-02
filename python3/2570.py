class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][0] <= nums2[p2][0]:
                if not res or nums1[p1][0] != res[-1][0]:
                    res.append(nums1[p1])
                else:
                    res[-1][1] += nums1[p1][1]
                p1 += 1
            else:
                if not res or nums2[p2][0] != res[-1][0]:
                    res.append(nums2[p2])
                else:
                    res[-1][1] += nums2[p2][1]
                p2 += 1
        while p1 < len(nums1):
            if not res or nums1[p1][0] != res[-1][0]:
                res.append(nums1[p1])
            else:
                res[-1][1] += nums1[p1][1]
            p1 += 1
        while p2 < len(nums2):
            if not res or nums2[p2][0] != res[-1][0]:
                res.append(nums2[p2])
            else:
                res[-1][1] += nums2[p2][1]
            p2 += 1
        return res
