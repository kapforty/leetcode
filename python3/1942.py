class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs, occupied = [i for i in range(len(times))], []
        heapq.heapify(chairs)
        
        for i in range(len(times)):
            times[i].append(i)
        times.sort(reverse=True)

        while times:
            arrival, leaving, friend = times.pop()
            while occupied and occupied[0][0] <= arrival:
                heapq.heappush(chairs, heapq.heappop(occupied)[1])
            if friend == targetFriend:
                return heapq.heappop(chairs)
            heapq.heappush(occupied, (leaving, heapq.heappop(chairs)))
