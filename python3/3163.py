class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        curr, count = word[0], 0
        for c in word:
            if count == 9 or c != curr:
                res += str(count) + curr
                curr = c
                count = 1
            else:
                count += 1
        res += str(count) + curr
        return res
