class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res = [1, 0]
        for c in s:
            w = widths[ord(c) - ord('a')]
            res[1] += w
            if res[1] > 100:
                res = [res[0] + 1, w]
        return res
