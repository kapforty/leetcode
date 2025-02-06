class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res, l, mapski = 0, len(nums), defaultdict(int)
        for i in range(l):
            for j in range(i + 1, l):
                mapski[nums[i] * nums[j]] += 1
        for k, v in mapski.items():
            res += v * (v-1) * 4
        return res
