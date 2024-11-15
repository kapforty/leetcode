class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:  
        # setup right pointer
        l, r = -1, len(arr) - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        res = r - l - 1
        
        # check for sorted array
        if res == 0:
            return 0
        
        # iterate through arr
        for l in range(len(arr)):
            if l > 0 and arr[l - 1] > arr[l]:
                break
            while r < len(arr) and arr[r] < arr[l]:
                r += 1
            res = min(res, r - l - 1)
        return res
