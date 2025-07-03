class Solution:
    def kthCharacter(self, k: int) -> str:
        word = [0]
        while len(word) < k:
            for i in range(len(word)):
                word.append(word[i] + 1)
        return chr(word[k-1] + ord('a'))
