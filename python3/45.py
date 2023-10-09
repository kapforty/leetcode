class Solution:
    def jump(self, nums: List[int]) -> int:
        res = currJump = nextJump = 0

        for num in nums[:-1]:
            currJump -= 1
            nextJump -= 1

            nextJump = max(nextJump, num)
            if currJump <= 0:
                res += 1
                currJump = nextJump

        return res

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         lenNums = len(nums)
#         res = [float("inf") for _ in range(lenNums)]
#         res[0] = 0

#         for i in range(lenNums - 1):
#             for j in range(i+1, i+1+nums[i]):
#                 if j == lenNums:
#                     break
#                 res[j] = min(res[j], res[i] + 1)

#         return res[-1]
