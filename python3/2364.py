class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mapski = defaultdict(int)
        for i, num in enumerate(nums):
            mapski[num - i] += 1
        res = comb(len(nums), 2)
        for k, v in mapski.items():
            if v > 1:
                res -= comb(v, 2)
        return res
