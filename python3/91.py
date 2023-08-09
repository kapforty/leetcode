class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        res = [0 for _ in range(len(s) + 2)]
        res[1] = 1
        res[2] = 1

        for i in range(1, len(s)):
            num1, num2 = int(s[i:i+1]), int(s[i-1:i+1])
            if num1 > 0:
                res[i+2] += res[i+1]
            else:
                res[i+2] = 0
            if num2 > 9 and num2 < 27:
                res[i+2] += res[i]
        
        return res[-1]
