class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr) - 1):
            curr = arr[i]
            for j in range(i+1, len(arr)):
                curr ^= arr[j]
                if curr == 0:
                    res += j - i
        return res
