class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        if words[0][0] != words[-1][-1]:
            return False
        for i in range(len(words) - 1):
            if words[i][-1] != words[i+1][0]:
                return False
        return True
