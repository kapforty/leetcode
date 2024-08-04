class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # calculate subarray sums
        subarraySums = []
        for i in range(len(nums)):
            curr = nums[i]
            subarraySums.append(curr)
            for j in range(i+1, len(nums)):
                curr += nums[j]
                subarraySums.append(curr)
        
        # sort subarray sums
        subarraySums.sort()

        # return sum of all values from indices left and right
        return sum(subarraySums[left-1:right]) % (10**9 + 7)
