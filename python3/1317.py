class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = [0, n]
        while str(res[0]).find("0") != -1 or str(res[1]).find("0") != -1:
            res[0] += 1
            res[1] -= 1
        return res
