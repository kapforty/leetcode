class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1, num2 = str(bin(num1))[2:], str(bin(num2))[2:]
        setBits = num2.count("1")
        
        res = []
        for c in num1:
            if not setBits:
                break
            if c == "1":
                res.append("1")
                setBits -= 1
            else:
                res.append("0")
                
        while len(res) < len(num1):
            res.append("0")

        res = ["0"] * setBits + res
        for i in range(len(res) - 1, -1, -1):
            if not setBits:
                break
            if res[i] == "0":
                res[i] = "1"
                setBits -= 1
        return int("".join(res), 2)
