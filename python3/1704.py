class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}

        one = s[:len(s)//2].lower()
        two = s[len(s)//2:].lower()

        countOne = countTwo = 0
        for char in one:
            if char in vowels:
                countOne += 1
        for char in two:
            if char in vowels:
                countTwo += 1

        return countOne == countTwo
