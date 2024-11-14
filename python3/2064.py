class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(amount):
            stores = 0
            for q in quantities:
                stores += ceil(q/amount)
            return stores <= n
        
        l, r = 1, max(quantities)
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l
