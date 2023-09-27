class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, prof = float("-inf"), 0

        for price in prices:
            buy = max(buy, prof - price)
            prof = max(prof, buy + price - fee)

        return prof
