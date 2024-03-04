class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -num)
        
        if not self.maxHeap:
            return

        while self.maxHeap[0] < -self.minHeap[0]:
            mini, maxi = heapq.heappop(self.minHeap), heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -maxi)
            heapq.heappush(self.maxHeap, -mini)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        else:
            return (-self.minHeap[0] + self.maxHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
