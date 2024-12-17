class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-ord(k), v))
        
        res = ""
        prev = []
        while heap:
            curr, count = heapq.heappop(heap)
            if prev:
                res += chr(-curr)
                count -= 1
                if count:
                    heapq.heappush(heap, (curr, count))
                heapq.heappush(heap, prev.pop())
            else:
                temp = min(repeatLimit, count)
                if temp == repeatLimit:
                    count -= temp
                    if count:
                        prev.append((curr, count))
                res += chr(-curr) * temp
        return res
