class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1, sentence2 = sentence1.split(" "), sentence2.split(" ")
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        while sentence1 and sentence2:
            if sentence1[-1] == sentence2[-1]:
                sentence1.pop()
                sentence2.pop()
            else:
                break
        
        sentence1, sentence2 = sentence1[::-1], sentence2[::-1]
        while sentence1 and sentence2:
            if sentence1[-1] == sentence2[-1]:
                sentence1.pop()
                sentence2.pop()
            else:
                break

        return not sentence1
