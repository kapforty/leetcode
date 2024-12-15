class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for x, y in classes:
            heapq.heappush(heap, (-((x+1)/(y+1) - x/y), (x,y)))
        
        for _ in range(extraStudents):
            x, y = heapq.heappop(heap)[1]
            x += 1
            y += 1
            heapq.heappush(heap, (-((x+1)/(y+1) - x/y), (x,y)))
        
        res = 0
        for x, y in heap:
            res += y[0]/y[1]
        return res / len(heap)
