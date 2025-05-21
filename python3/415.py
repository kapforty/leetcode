class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # pad nums to equal length
        while len(num1) < len(num2):
            num1 = "0" + num1
        while len(num1) > len(num2):
            num2 = "0" + num2
        
        # elementary arithmetic (addition)
        res, carry = "", 0
        for i in range(len(num1)-1, -1, -1):
            curr = int(num1[i]) + int(num2[i]) + carry
            res = str(curr % 10) + res
            carry = curr // 10
        return res if not carry else str(carry) + res
