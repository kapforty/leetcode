class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = False

        # trivial case
        if len(num) < 3:
            return res

        def backtrack(curr, l, m, r):
            nonlocal res
            if res or r >= len(curr) or (m-l > 1 and curr[l] == "0") or (r-m > 1 and curr[m] == "0") or m-l > len(curr[r:]):
                return
            first, second = curr[:m], curr[m:r]
            search = str(int(first) + int(second))
            if search == curr[r:]:
                res = True
                return
            if curr[r:].find(search) == 0:
                backtrack(curr[m:], 0, 1, 2)
            backtrack(curr, l, m+1, r+1)
            backtrack(curr, l, m, r+1)
            
        backtrack(num, 0, 1, 2)
        return res
