class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        return even + odd

# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         res = deque()
        
#         for num in nums:
#             if num % 2 == 0:
#                 res.appendleft(num)
#             else:
#                 res.append(num)
        
#         return res
