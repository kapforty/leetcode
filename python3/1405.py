class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            heapq.heappush(maxHeap, (-a, "a"))
        if b > 0:
            heapq.heappush(maxHeap, (-b, "b"))
        if c > 0:
            heapq.heappush(maxHeap, (-c, "c"))
        blocked = []

        res = ""
        while maxHeap:
            if len(res) >= 2 and res[-1] == res[-2] == maxHeap[0][1]:
                blocked.append(heapq.heappop(maxHeap))
                continue
            count, char = heapq.heappop(maxHeap)
            res += char
            count += 1
            if count < 0:
                heapq.heappush(maxHeap, (count, char))
            if blocked:
                heapq.heappush(maxHeap, blocked.pop())
        return res
