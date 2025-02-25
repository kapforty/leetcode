class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = curr = 0
        counts = [1, 0]
        for num in arr:
            curr += num
            res += counts[(curr + 1) % 2]
            counts[curr % 2] += 1
        return res % (10**9 + 7)
