class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        l, r = 0, 2**(n-1)-1
        curr = 0

        while l < r:
            mid = (l + r)/2
            if k < mid:
                r = floor(mid)
            else:
                curr = 1 if curr == 0 else 0
                l = ceil(mid)

        return curr
