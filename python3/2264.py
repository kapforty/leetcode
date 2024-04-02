class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(1, len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                res = max(res, int(num[i]))
        return "" if res == -1 else str(res) * 3
