class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        res, day, pq = 0, 1, []
        while events or pq:
            while events and events[-1][0] == day:
                heappush(pq, events.pop()[1])
            while pq and pq[0] < day:
                heappop(pq)
            if pq and pq[0] >= day:
                heappop(pq)
                res += 1
            day += 1
        return res
