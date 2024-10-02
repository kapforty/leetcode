class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))
        rankMap = defaultdict(int)
        for i, val in enumerate(sortedArr): 
            rankMap[val] = i + 1
        res = []
        for val in arr: 
            res.append(rankMap[val])
        return res
