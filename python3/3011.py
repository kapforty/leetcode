class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        curr = str(bin(nums[0]))[2:].count("1")
        currMin = currMax = nums[0]
        rangeMinAndMax = []
        for num in nums:
            temp = str(bin(num))[2:].count("1")
            if temp != curr:
                rangeMinAndMax.append([currMin, currMax])
                currMin = currMax = num
                curr = temp
            else:
                currMin = min(currMin, num)
                currMax = max(currMax, num)
        rangeMinAndMax.append([currMin, currMax])
        for i in range(len(rangeMinAndMax) - 1):
            if rangeMinAndMax[i][1] > rangeMinAndMax[i+1][0]:
                return False
        return True
