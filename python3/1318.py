class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a > 0 or b > 0 or c > 0:
            currA, currB, currC = a & 1, b & 1, c & 1
            if currC == 0:
                res += currA + currB
            else:
                if currA == 0 and currB == 0:
                    res += 1  
            a >>= 1
            b >>= 1
            c >>= 1
        return res

# class Solution:
#     def minFlips(self, a: int, b: int, c: int) -> int:
#         res = 0

#         while a > 0 or b > 0 or c > 0:
#             currA, currB, currC = a%2, b%2, c%2
#             if currC == 0:
#                 if currA == 1: res += 1
#                 if currB == 1: res += 1
#             else:
#                 if currA == 0 and currB == 0:
#                     res += 1
#             a, b, c = a//2, b//2, c//2

#         return res
