class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float("inf")] * k
        profit = [0] * k
        for price in prices:
            for i in range(k):
                if i == 0:
                    buy[0] = min(buy[0], price)
                else:
                    buy[i] = min(buy[i], price - profit[i-1])
                profit[i] = max(profit[i], price - buy[i]) 
        return profit[-1]
