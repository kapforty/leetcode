class Solution:
    def isValid(self, word: str) -> bool:
        vowels = consonant = 0
        if len(word) < 3:
            return False
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in "aeiouAEIOU":
                    vowels += 1
                else:
                    consonant += 1
        if not vowels or not consonant:
            return False
        return True
