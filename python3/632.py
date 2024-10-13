class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # initialize minHeap and maxHeap
        minHeap, maxHeap = [(-inf, i, -1) for i in range(len(nums))], []
        heapq.heapify(minHeap)
        
        # remove smallest element in minHeap
        # push next value in list into minHeap and maxHeap
        res = None
        smallestRange = inf
        while True:
            num, arr, idx = heapq.heappop(minHeap)
            if idx + 1 >= len(nums[arr]):
                break
            heapq.heappush(minHeap, (nums[arr][idx + 1], arr, idx + 1))
            heapq.heappush(maxHeap, -nums[arr][idx + 1])
            if -maxHeap[0] - minHeap[0][0] < smallestRange:
                smallestRange = -maxHeap[0] - minHeap[0][0]
                res = [minHeap[0][0], -maxHeap[0]]
        return res
