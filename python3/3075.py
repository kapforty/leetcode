class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # build heap/priority queue
        pq = []
        for val in happiness:
            heapq.heappush(pq, -val)
        
        # pop elements from pq
        happinessValue = sum(happiness)
        res = 0
        for i in range(k):
            curr = None
            while happinessValue - i - -pq[0] < 0:
                heapq.heappop(pq)
            if -pq[0] - i <= 0:
                break
            res += -heapq.heappop(pq) - i
        
        return res
