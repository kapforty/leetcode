class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def bt(i):
            nonlocal k
            if i == n:
                k -= 1
                return True if k == 0 else False
            for c in "abc":
                if res and ((res[-1] == c == "a") or (res[-1] == c == "b") or (res[-1] == c == "c")):
                    continue
                res.append(c)
                if bt(i + 1):
                    return True
                res.pop()
            return False
        bt(0)
        return "".join(res)
