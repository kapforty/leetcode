class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix, postfix = [], deque()

        # calculate prefix
        temp = -1
        for i, val in enumerate(nums[:-1]):
            prefix.append(temp)
            if nums[i] % 2 == nums[i + 1] % 2:
                temp = i
        prefix.append(temp)

        # calculate postfix
        temp = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            postfix.appendleft(temp)
            if nums[i] % 2 == nums[i - 1] % 2:
                temp = i
        postfix.appendleft(temp)

        res = []
        for x, y in queries:
            res.append(True if postfix[x] > y and prefix[y] < x else False)
        return res
