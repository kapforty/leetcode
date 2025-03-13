class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diffArr = [0] * (len(nums) + 1)
        currDiff = idx = q = 0
        while idx < len(nums):
            # update currDiff
            if diffArr[idx] != 0:
                currDiff += diffArr[idx]
                diffArr[idx] = 0
            # shift idx if valid
            if nums[idx] - currDiff <= 0:
                idx += 1
                continue
            # update difference array if invalid
            if q == len(queries):
                return -1
            l, r, v = queries[q]
            if l < idx <= r:
                currDiff += v
            if r >= idx:
                diffArr[l] += v
                diffArr[r + 1] -= v 
            q += 1
        return q
