class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        strArr = list(s)

        l, r = 0, len(s) - 1

        while l < r:
            if strArr[l] not in vowelSet:
                l += 1
                continue
            if strArr[r] not in vowelSet:
                r -= 1
                continue
            temp = strArr[l]
            strArr[l] = strArr[r]
            strArr[r] = temp
            l += 1
            r -= 1
        
        return "".join(strArr)
            
