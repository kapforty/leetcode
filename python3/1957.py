class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) >= 2 and c == res[-1] == res[-2]:
                continue
            res.append(c)
        return "".join(res)
