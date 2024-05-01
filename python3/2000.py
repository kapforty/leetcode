class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        prefix = word[:idx+1]
        return prefix[::-1] + word[idx+1:]
