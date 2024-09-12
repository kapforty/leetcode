class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        allowed = set(allowed)
        for word in words:
            if set(word).issubset(allowed):
                res += 1
        return res
