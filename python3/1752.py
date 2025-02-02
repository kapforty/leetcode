class Solution:
    def check(self, nums: List[int]) -> bool:
        target = deque(sorted(nums))
        nums = deque(nums)
        for _ in range(len(nums)):
            if nums == target:
                return True
            nums.append(nums.popleft())
        return False
