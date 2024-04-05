class Solution:
    def makeGood(self, s: str) -> str:
        res = [s[0]]
        for char in s[1:]:
            if res and char.lower() == res[-1].lower() and ord(char) != ord(res[-1]):
                res.pop()
                continue
            res.append(char)
        return "".join(res)
