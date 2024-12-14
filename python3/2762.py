class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = res = 0
        low, high = [], []
        for r in range(len(nums)):
            res += r - l
            heapq.heappush(low, (nums[r], r))
            heapq.heappush(high, (-nums[r], r))
            while -high[0][0] - low[0][0] > 2:
                if low[0][1] <= high[0][1]:
                    l = max(l, heapq.heappop(low)[1] + 1)
                else:
                    l = max(l, heapq.heappop(high)[1] + 1)
        return res + r - l + 1
