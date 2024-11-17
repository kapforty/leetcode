class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res, deq = inf, deque()
        for idx, num in enumerate(nums):
            curr = (num + (deq[-1][0] if deq else 0), idx)
            while deq and curr[0] < deq[-1][0]:
                deq.pop()
            deq.append(curr)
            if deq[-1][0] >= k:
                res = min(res, deq[-1][1] + 1)
            while deq and deq[-1][0] - deq[0][0] >= k:
                res = min(res, deq[-1][1] - deq[0][1])
                deq.popleft()
        return -1 if res == inf else res
