class Solution:
    def findComplement(self, num: int) -> int:
        curr = 1
        while curr <= num:
            curr *= 2
        return (curr - 1) ^ num
