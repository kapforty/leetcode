class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # get indices of each char
        a, b, c = [], [], []
        for i, char in enumerate(s):
            if char == "a":
                a.append(i)
            elif char == "b":
                b.append(i)
            elif char == "c":
                c.append(i)
        
        # calculate result
        res = 0
        while a and b and c:
            left, right = min(a[-1], b[-1], c[-1]), max(a[-1], b[-1], c[-1])
            res += left + 1
            if right == a[-1]:
                a.pop()
            elif right == b[-1]:
                b.pop()
            else:
                c.pop()
        return res
