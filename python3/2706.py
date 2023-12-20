class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        cost = money - sum(prices[:2])
        if cost >= 0 and cost < money:
            return cost
        return money
