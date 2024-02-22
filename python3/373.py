class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], [i, 0]))
        for _ in range(k):
            x, y = heapq.heappop(heap)[1]
            if y + 1 < len(nums2):
                heapq.heappush(heap, (nums1[x] + nums2[y + 1], [x, y + 1]))
            res.append([nums1[x], nums2[y]])
        return res
