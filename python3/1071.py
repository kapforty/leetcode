class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""

        if str1 + str2 != str2 + str1:
            return res

        str1Len = len(str1)
        str2Len = len(str2)
        minLen = min(str1Len, str2Len)

        for i in range(1, minLen+1, 1):
            if str1Len % i != 0 or str2Len % i != 0:
                continue
            if str1[0:i]*(str1Len//i) != str1:
                continue
            if str2[0:i]*(str2Len//i) != str2:
                continue
            res = str1[0:i]
        
        return res
