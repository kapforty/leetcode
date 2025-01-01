class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1, set2, set3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            curr = set(word.lower())
            if len(set1 | curr) == len(set1) or len(set2 | curr) == len(set2) or len(set3 | curr) == len(set3):
                res.append(word)
        return res
