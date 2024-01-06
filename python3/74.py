class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # convert to one-dimensional array
        arr = []
        for row in matrix:
            arr += row
        
        # binary search
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l+r) // 2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid

        return True if arr[l] == target else False
