class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        res = 0
        while k > 0:
            if k >= chalk[res]:
                k -= chalk[res]
                res += 1
            else:
                return res
        return res
