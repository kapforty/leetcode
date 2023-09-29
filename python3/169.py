class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0

        for num in nums:
            if num == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = num
                    count += 1
                else:
                    count -= 1

        return candidate

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         numsCounter = Counter(nums)
#         for k in numsCounter:
#             if numsCounter[k] > len(nums) / 2:
#                 return k
