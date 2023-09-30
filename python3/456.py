class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        currMin = nums[0]
        stack = []

        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True
            stack.append([num, currMin])
            currMin = min(currMin, num)

        return False
