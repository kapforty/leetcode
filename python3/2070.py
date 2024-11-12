class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # calculate max beauty for each price in items
        beautyMap = defaultdict(int)
        maxVal = 0
        items.sort()
        for x, y in items:
            maxVal = max(maxVal, y)
            beautyMap[x] = max(beautyMap[x], maxVal)

        # binary search
        prices = list(beautyMap.keys())
        res = []
        for q in queries:
            if q < prices[0]:
                res.append(0)
                continue
            l, r = 0, len(prices) - 1
            while l < r:
                m = (l + r + 1) // 2
                if prices[m] <= q:
                    l = m
                else:
                    r = m - 1
            res.append(beautyMap[prices[l]])
        return res
