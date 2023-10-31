class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        while words[-1] == "":
            words.pop()
        return len(words[-1])
