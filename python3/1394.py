class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res, counter = -1, Counter(arr)
        for k, v in counter.items():
            if k == v:
                res = max(res, k)
        return res
