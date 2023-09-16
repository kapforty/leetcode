class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0

        for num in nums:
            if counter[num] > 0:
                counter[num] -= 1
                if counter[k-num] > 0:
                    counter[k-num] -= 1
                    res += 1
                else:
                    counter[num] += 1
        return res

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         l, r = 0, len(nums) - 1
#         res = 0

#         while l < r:
#             currSum = nums[l] + nums[r]
#             if currSum == k:
#                 res += 1
#                 l += 1
#                 r -= 1
#             elif currSum < k:
#                 l += 1
#             else:
#                 r -= 1
        
#         return res
