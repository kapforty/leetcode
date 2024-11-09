class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for acc in accounts:
            res = max(res, sum(acc))
        return res
