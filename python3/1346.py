class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        if arr[0] > 1:
            return True
        for val in arr:
            if val != 0 and val * 2 in arr:
                return True
        return False
