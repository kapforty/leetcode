class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        for left, right in intervals:
            if minHeap and minHeap[0] < left:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, right)
        return len(minHeap)
