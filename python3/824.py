class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split(" ")
        for i in range(len(s)):
            if s[i][0] in "aeiouAEIOU":
                s[i] += "ma"
            else:
                s[i] = s[i][1:] + s[i][0] + "ma"
            for _ in range(i+1):
                s[i] += "a"
        return " ".join(s)
