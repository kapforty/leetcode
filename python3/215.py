# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k

#         def quickSelect(l, r):
#             p, pivot = l, nums[r]
#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]
#             if p < k:
#                 return quickSelect(p+1, r)
#             elif p > k:
#                 return quickSelect(l, p-1)
#             else:
#                 return nums[p]

#         return quickSelect(0, len(nums) - 1)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

        return heap[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[len(nums) - k]
