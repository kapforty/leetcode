class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n-1):
            temp, curr, count = "", res[0], 1
            for c in res[1:]:
                if c != curr:
                    temp += str(count) + curr
                    curr, count = c, 1
                else:
                    count += 1
            res = temp + str(count) + curr
        return res
