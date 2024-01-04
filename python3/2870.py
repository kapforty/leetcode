class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        counter = Counter(nums)
        for num in counter:
            if counter[num] == 1:
                return -1
            res += counter[num]//3
            if counter[num]%3 != 0:
                res += 1
        return res
