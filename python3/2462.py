class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap1, heap2 = [], []
        l, r = 0, len(costs) - 1
        res = 0

        for i in range(k):
            while len(heap1) < candidates and l <= r:
                heapq.heappush(heap1, costs[l])
                l += 1
            while len(heap2) < candidates and l <= r:
                heapq.heappush(heap2, costs[r])
                r -= 1

            cost1 = heap1[0] if heap1 else float("inf")
            cost2 = heap2[0] if heap2 else float("inf")
            
            if cost1 <= cost2:
                res += cost1
                heapq.heappop(heap1)
            else:
                res += cost2
                heapq.heappop(heap2)
        return res

# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         heap1, heap2 = [], []
#         heapq.heapify(heap1)
#         heapq.heapify(heap2)
#         res = 0
        
#         for _ in range(candidates):
#             if not costs:
#                 break
#             elif len(costs) == 1:
#                 heapq.heappush(heap1, costs.pop(0))
#             else:
#                 heapq.heappush(heap1, costs.pop(0))
#                 heapq.heappush(heap2, costs.pop())
        
#         for i in range(k):
#             cost1 = heap1[0] if heap1 else float("inf")
#             cost2 = heap2[0] if heap2 else float("inf")
            
#             if cost1 <= cost2:
#                 res += cost1
#                 heapq.heappop(heap1)
#                 if costs:
#                     heapq.heappush(heap1, costs.pop(0))
#             else:
#                 res += cost2
#                 heapq.heappop(heap2)
#                 if costs:
#                     heapq.heappush(heap2, costs.pop())
#         return res

        
