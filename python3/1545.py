class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res = "0"
        for _ in range(n - 1):
            res = res + "1" + ''.join('1' if x == '0' else '0' for x in res[::-1])
        return res[k - 1]
