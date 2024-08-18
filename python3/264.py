class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        visited = set()
        heapq.heappush(heap, 1)
        count, curr = 0, None
        while count < n:
            count += 1
            curr = heapq.heappop(heap)
            if curr * 2 not in visited:
                visited.add(curr * 2)
                heapq.heappush(heap, curr * 2)
            if curr * 3 not in visited:
                visited.add(curr * 3)
                heapq.heappush(heap, curr * 3)
            if curr * 5 not in visited:
                visited.add(curr * 5)
                heapq.heappush(heap, curr * 5)
        return curr
