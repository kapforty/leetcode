class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res, deq = [], deque()
        for i in range(len(nums)):
            if len(deq) == k: 
                deq.popleft()
            if deq and deq[-1] != nums[i] - 1: 
                deq = deque()
            deq.append(nums[i])
            res.append(deq[-1] if len(deq) == k else -1)
        return res[k-1:]
