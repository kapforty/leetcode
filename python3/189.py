class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        lenNums = len(nums)
        k %= lenNums
        nums.reverse() 
        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range((lenNums - k)//2):
            nums[i + k], nums[lenNums-1-i] = nums[lenNums-1-i], nums[i + k]

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         for _ in range(k):
#             nums.insert(0, nums.pop())  
