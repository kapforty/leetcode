class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # sort workers by rate (increasing)
        workers = []
        for i in range(len(wage)):
            workers.append([wage[i]/quality[i], quality[i]])
        workers.sort()

        # calculate min cost
        res = float("inf")
        hired = []
        totalQuality = 0
        for rate, q in workers:
            while len(hired) >= k and hired[0] < -q:
                totalQuality += heapq.heappop(hired)
            if len(hired) < k:
                heapq.heappush(hired, -q)
                totalQuality += q
            if len(hired) == k:
                res = min(res, totalQuality * rate)
        return res
