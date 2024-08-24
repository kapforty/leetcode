class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            res = res * 26 + ord(char) - ord("@")
        return res
