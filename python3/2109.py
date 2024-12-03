class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        for i, end in enumerate(spaces):
            start = spaces[i-1] if i > 0 else 0
            res.append(s[start:end])
        res.append(s[end:])
        return " ".join(res)
