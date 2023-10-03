class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        
        for ele in counter:
            for i in range(1, counter[ele]):
                res += i

        return res
