class Solution:
    def partitionString(self, s: str) -> int:
        currChars = set()
        res = 0
        for char in s:
            if char in currChars:
                res += 1
                currChars = set()
            currChars.add(char)
        return res + 1
