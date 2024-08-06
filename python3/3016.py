class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        heap = []
        heapq.heapify(heap)

        for k, v in counter.items():
            heapq.heappush(heap, [-v, k])
        
        cost = 1
        remaining = 8
        res = 0

        while heap:
            res += -heapq.heappop(heap)[0] * cost
            remaining -= 1
            if remaining == 0:
                remaining = 8
                cost += 1
        
        return res
