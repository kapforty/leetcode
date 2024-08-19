class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while startValue != target:
            if startValue > target:
                res += startValue - target
                break
            if target % 2 == 0:
                target //= 2
                res += 1
            else:
                target += 1
                res += 1
        return res
