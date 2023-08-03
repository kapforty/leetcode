class Solution:
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0

        for num in nums:
            temp = max(num + l, r)
            l = r
            r = temp
        
        return r

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         maxMoney = [0 for _ in range(len(nums))]

#         maxMoney[0], maxMoney[1] = nums[0], nums[1]
#         if maxMoney[1] < maxMoney[0]:
#             maxMoney[1] = maxMoney[0] 

#         for i in range(2, len(nums), 1):
#             maxMoney[i] = max(maxMoney[i-2] + nums[i], maxMoney[i-1])
        
#         return maxMoney[-1]
        
