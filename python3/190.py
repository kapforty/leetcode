class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            curr = n >> i & 1
            res = res | curr << (31 - i)
        return res
