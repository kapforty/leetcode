class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i, val in enumerate(nums):
            if dq: nums[i] += nums[dq[0]]

            while dq and (nums[dq[0]] <= nums[i] or k <= i - dq[0]):
                dq.popleft()

            if nums[i] > 0:
                while dq and nums[dq[-1]] <= nums[i]:
                    dq.pop()
                dq.append(i)
                
        return max(nums)
