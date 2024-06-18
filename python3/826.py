class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff = []
        for i in range(len(profit)):
            diff.append((difficulty[i], profit[i]))
        diff.sort()
        worker.sort()

        maxProfit = res = 0
        i = -1
        for w in worker:
            while i < len(diff) - 1 and diff[i + 1][0] <= w:
                i += 1
                maxProfit = max(maxProfit, diff[i][1])
            res += maxProfit

        return res
