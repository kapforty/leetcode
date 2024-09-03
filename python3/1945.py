class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # convert
        convert = ""
        for char in s:
            convert += str(ord(char) - ord('a') + 1)
        
        # transform
        res = int(convert)
        for _ in range(k):
            temp = 0
            while res > 0:
                temp += res % 10
                res //= 10
            res = temp
        return res
