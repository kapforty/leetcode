class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i] 
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         numsSum = sum(nums)
#         leftSum = 0
#         for i in range(len(nums)):
#             if leftSum*2 + nums[i] == numsSum:
#                 return i
#             leftSum += nums[i]       
#         return -1
