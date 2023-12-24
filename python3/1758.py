class Solution:
    def minOperations(self, s: str) -> int:
        res = float("inf")

        curr = "0"
        flips = 0
        for char in s:
            if char != curr:
                flips += 1
            curr = "1" if curr == "0" else "0"
        res = min(res, flips)
        
        curr = "1"
        flips = 0
        for char in s:
            if char != curr:
                flips += 1
            curr = "1" if curr == "0" else "0"
        res = min(res, flips)

        return res
