class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        for i in range(len(prices) - 1, -1, -1):
            while prices[i] < stack[-1]:
                stack.pop()
            prices[i] -= stack[-1]
            stack.append(prices[i] + stack[-1])
        return prices
