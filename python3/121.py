class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = float("inf")

        for price in prices:
            if price < prev:
                prev = price
            else:
                res = max(res, price - prev)

        return res
