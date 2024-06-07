class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        res = []
        sentence = sentence.split(" ")
        for word in sentence:
            found = False
            for i in range(len(word)):
                if word[:i] in dictionary:
                    res.append(word[:i])
                    found = True
                    break
            if not found:
                res.append(word)
        return " ".join(res)
