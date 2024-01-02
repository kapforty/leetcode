class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = defaultdict(list)
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1

        for k, v in numMap.items():
            for i in range(v):
                res[i].append(k)

        return res.values()
