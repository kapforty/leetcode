class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        res = 0
        for price in prices:
            if price < mini:
                mini = price
            res = max(res, price - mini)
        return res
