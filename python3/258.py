class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            curr = 0
            for char in num:
                curr += int(char)
            num = str(curr)
        return int(num)