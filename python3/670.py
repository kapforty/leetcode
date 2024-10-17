class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        maxHeap = []
        for i, c in enumerate(num):
            heapq.heappush(maxHeap, (-int(c), -i))
        
        for i, c in enumerate(num):
            while maxHeap and -maxHeap[0][1] <= i:
                heapq.heappop(maxHeap)
            if not maxHeap:
                break
            if -maxHeap[0][0] > int(c):
                num[i], num[-maxHeap[0][1]] = num[-maxHeap[0][1]], num[i]
                break
        
        return int("".join(num))
