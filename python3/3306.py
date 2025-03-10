class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helper(k):
            vowels, consonants = {"a":0, "e":0, "i":0, "o":0, "u":0}, 0
            count = l = r = 0
            while r < len(word):
                if word[r] in "aeiou":
                    vowels[word[r]] += 1
                else:
                    consonants += 1
                r += 1
                while consonants >= k and list(vowels.values()).count(0) == 0:
                    count += len(word) - r + 1
                    if word[l] in "aeiou":
                        vowels[word[l]] -= 1
                    else:
                        consonants -= 1
                    l += 1
            return count
        return helper(k) - helper(k+1)
