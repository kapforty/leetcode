class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddIndexes = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                oddIndexes.append(i)
        
        k -= 1
        ptr = k
        if ptr >= len(oddIndexes):
            return 0

        res = 0
        while ptr < len(oddIndexes):
            if ptr-k == 0:
                left = oddIndexes[ptr-k] + 1
            else:
                left = oddIndexes[ptr-k] - oddIndexes[ptr-k-1] if ptr-k-1 >= 0 else 1
            if ptr == len(oddIndexes) - 1:
                right = len(nums) - oddIndexes[ptr]
            else:
                right = oddIndexes[ptr+1] - oddIndexes[ptr] if ptr+1 < len(oddIndexes) else 1
            ptr += 1
            res += left * right

        return res
