class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = largestVal = 0

        for char in s[::-1]:
            if numerals[char] < largestVal:
                res -= numerals[char]
            else:
                res += numerals[char]
            largestVal = max(largestVal, numerals[char])
        
        return res
