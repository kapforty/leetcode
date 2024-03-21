class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countOnes = s.count("1")
        sLen = len(s)
        res = ""
        for _ in range(countOnes - 1):
            res += "1"
        for _ in range(sLen - countOnes):
            res += "0"
        return res + "1"
