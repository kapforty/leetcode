class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = []
        for word in words[::-1]:
            if word == "":
                continue
            res.append(word)
        return " ".join(res)
