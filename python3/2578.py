class Solution:
    def splitNum(self, num: int) -> int:
        nums = []
        for c in str(num):
            nums.append(c)
        nums.sort()
        num1, num2 = [], []
        for i, val in enumerate(nums):
            if i % 2 != 0:
                num1.append(val)
            else:
                num2.append(val)
        return int("".join(num1)) + int("".join(num2))
