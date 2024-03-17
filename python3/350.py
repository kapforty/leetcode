class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map, nums2Map = defaultdict(int), defaultdict(int)
        res = []
        for num in nums1:
            nums1Map[num] += 1
        for num in nums2:
            nums2Map[num] += 1
        for k, v in nums1Map.items():
            for i in range(min(v, nums2Map[k])):
                res.append(k)
        return res
