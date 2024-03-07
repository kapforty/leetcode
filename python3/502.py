class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []

        # sort projects by capacity
        projects = []
        for i in range(len(profits)):
            projects.append((capital[i], profits[i]))
        projects.sort(reverse=True)
        
        # push projects onto heap (if you have enough capital)
        while k > 0:
            while projects and projects[-1][0] <= w:
                heapq.heappush(heap, -projects.pop()[1])
            if len(heap) == 0:
                break
            w += -heapq.heappop(heap)
            k -= 1

        return w
