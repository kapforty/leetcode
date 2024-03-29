class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        words = text.split(" ")
        brokenLetters = set(brokenLetters)

        for word in words:
            word = set(word)
            if len(word.intersection(brokenLetters)) == 0:
                res += 1
        
        return res