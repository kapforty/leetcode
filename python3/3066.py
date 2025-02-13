class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        while nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            res += 1
        return res
