class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        currMax, currMin = 1, 1
        
        for num in nums:
            temp = currMax * num
            currMax = max(temp, currMin*num, num)
            currMin = min(temp, currMin*num, num)
            res = max(res, currMax)
        return res    
