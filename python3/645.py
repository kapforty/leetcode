class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numMap = defaultdict(int)
        for val in nums:
            numMap[val] += 1
        res1, res2 = None, None
        for i in range(1, len(nums) + 1):
            if i not in numMap:
                res2 = i
                continue
            if numMap[i] == 2:
                res1 = i
        return [res1, res2]
        
