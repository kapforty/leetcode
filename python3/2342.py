class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res, mapski = -1, defaultdict(list)
        for num in nums:
            currSum, numStr = 0, str(num)
            for c in numStr:
                currSum += int(c)
            heappush(mapski[currSum], -num)
        for k, v in mapski.items():
            if len(v) >= 2:
                res = max(res, -heappop(v) - heappop(v))
        return res
