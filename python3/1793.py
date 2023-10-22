class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        leftStack, rightStack = nums[:k], nums[:k:-1] 
        interval = 1
        minVal = res = nums[k]

        while leftStack or rightStack:
            if not leftStack:
                curr = rightStack.pop()
            elif not rightStack or leftStack[-1] >= rightStack[-1]:
                curr = leftStack.pop()
            else:
                curr = rightStack.pop()
            minVal = min(minVal, curr)
            interval += 1 
            res = max(res, minVal * interval)
        
        return res
