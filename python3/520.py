class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower() or (word[0] == word[0].upper() and word[1:] == word[1:].lower()):
            return True
        return False
